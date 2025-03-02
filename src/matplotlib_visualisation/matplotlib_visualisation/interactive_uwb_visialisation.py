import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path
from matplotlib.widgets import Button, Slider
from shapely.geometry import Point
import matplotlib.animation as animation


class UWBVisualization:
    """Main class for UWB ranging and position estimation visualization."""
    
    def __init__(self):
        """Initialize the visualization environment."""
        self.fig = plt.figure(figsize=(12, 9))
        self.ax = self.fig.add_subplot(111)
        self.ax.grid(True)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_aspect('equal')
        self.ax.set_title('UWB Positioning Visualization', fontsize=14)
        
        # Set up anchor position (fixed reference point)
        self.anchor_pos = (0, 0)
        self.ax.plot(*self.anchor_pos, 'o', color='red', markersize=8, label='Anchor')
        
        # Standard deviation for distance measurement (measurement error)
        self.std_dev = 0.1
        
        # Initialize storage for all ranging points
        self.ranging_points = []
        
        # Initialize drone path visualization elements
        self.path_line = None
        self.position_estimate = None
        self.history_points = []
        
        # Initialize animation elements
        self.animation = None
        self.is_animating = False
        
        # Setup UI controls
        self._setup_controls()
        
        # Setup intersection visualization elements
        self.intersection_patch = None
        self.intersection_area_text = None
        self.gdop_text = None
        self.accuracy_circle = None
        
        # Add initial ranging point
        self._add_ranging_point()
        
        # Set up legend and status text
        self.ax.legend(loc='upper right')
        self.status_text = self.ax.text(
            0.02, 0.98, 
            "Ready", 
            transform=self.ax.transAxes,
            verticalalignment='top',
            fontsize=10
        )
        
        # Setup keyboard handler for closing the plot with Ctrl+C
        self.fig.canvas.mpl_connect('key_press_event', self._on_key_press)

    def _setup_controls(self):
        """Setup UI controls like buttons and sliders."""
        # Add button
        ax_add_button = plt.axes([0.75, 0.05, 0.1, 0.04])
        self.add_button = Button(ax_add_button, 'Add Point')
        self.add_button.on_clicked(self._add_ranging_point_callback)
        
        # Clear path button
        ax_clear_button = plt.axes([0.87, 0.05, 0.1, 0.04])
        self.clear_button = Button(ax_clear_button, 'Clear Path')
        self.clear_button.on_clicked(self._clear_path_callback)
        
        # Animation control button
        ax_anim_button = plt.axes([0.75, 0.10, 0.1, 0.04])
        self.anim_button = Button(ax_anim_button, 'Animate Path')
        self.anim_button.on_clicked(self._toggle_animation_callback)
        
        # Export button
        ax_export_button = plt.axes([0.87, 0.10, 0.1, 0.04])
        self.export_button = Button(ax_export_button, 'Export Data')
        self.export_button.on_clicked(self._export_data_callback)
        
        # Error slider
        ax_slider = plt.axes([0.15, 0.02, 0.5, 0.03])
        self.std_dev_slider = Slider(
            ax_slider, 'Error (%)', 
            1, 25, 
            valinit=self.std_dev*100, 
            valstep=1
        )
        self.std_dev_slider.on_changed(self._update_std_dev)

    def _add_ranging_point_callback(self, event):
        """Callback for the Add Point button."""
        self._add_ranging_point()
        self._update_path()
        plt.draw()

    def _clear_path_callback(self, event):
        """Callback for clearing the drone path."""
        self.ranging_points = []
        self.history_points = []
        
        # Clear the visualization
        self.ax.cla()
        self.ax.grid(True)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_title('UWB Positioning Visualization', fontsize=14)
        
        # Reset anchor
        self.ax.plot(*self.anchor_pos, 'o', color='red', markersize=8, label='Anchor')
        self.ax.legend(loc='upper right')
        
        # Reset intersection visualization
        self.intersection_patch = None
        self.intersection_area_text = None
        self.gdop_text = None
        
        # Add initial point
        self._add_ranging_point()
        
        # Update status
        self._update_status("Path cleared")
        plt.draw()

    def _toggle_animation_callback(self, event):
        """Toggle animation of the drone path."""
        if not self.is_animating and len(self.ranging_points) > 1:
            self.is_animating = True
            self.anim_button.label.set_text('Stop Anim')
            self._start_animation()
        else:
            self.is_animating = False
            self.anim_button.label.set_text('Animate Path')
            if self.animation:
                self.animation.event_source.stop()
            self._update_status("Animation stopped")

    def _start_animation(self):
        """Start the animation of drone movement along the path."""
        if len(self.ranging_points) < 2:
            self._update_status("Need at least 2 points for animation")
            return
        
        # Create a drone marker
        if not hasattr(self, 'drone_marker'):
            self.drone_marker = self.ax.plot([], [], 'o', color='green', markersize=10)[0]
        
        # Interpolate more points along the path for smoother animation
        points = np.array([p.center for p in self.ranging_points])
        t = np.arange(len(points))
        t_interp = np.linspace(0, len(points)-1, num=100)
        x_interp = np.interp(t_interp, t, points[:, 0])
        y_interp = np.interp(t_interp, t, points[:, 1])
        interp_points = np.column_stack((x_interp, y_interp))
        
        # Animation update function
        frame_count = [0]
        max_frames = len(interp_points)
        
        def update(frame):
            if frame_count[0] >= max_frames:
                frame_count[0] = 0
            
            pos = interp_points[frame_count[0]]
            self.drone_marker.set_data([pos[0]], [pos[1]])
            frame_count[0] += 1
            
            # Visualize current range
            self._simulate_range_at_position(pos)
            return self.drone_marker,
        
        self.animation = animation.FuncAnimation(
            self.fig, update, frames=max_frames,
            interval=50, blit=True, repeat=True
        )
        
        self._update_status("Animation started")

    def _simulate_range_at_position(self, position):
        """Simulate UWB range readings from current position."""
        # If we already have a simulated circle, remove it
        if hasattr(self, 'sim_range') and self.sim_range:
            self.sim_range.remove()
            
        # Calculate true distance to anchor
        distance = np.linalg.norm(np.array(position) - np.array(self.anchor_pos))
        
        # Add some simulated measurement noise
        noisy_distance = distance * (1 + np.random.normal(0, self.std_dev/2))
        
        # Draw the range circle
        self.sim_range = plt.Circle(
            position, noisy_distance, 
            color='green', fill=False, 
            linestyle='--', alpha=0.7
        )
        self.ax.add_patch(self.sim_range)
        
    def _export_data_callback(self, event):
        """Export the current configuration and data."""
        if len(self.ranging_points) == 0:
            self._update_status("No data to export")
            return
            
        try:
            # Prepare data for export
            data = {
                'anchor_position': self.anchor_pos,
                'std_dev': self.std_dev,
                'points': [p.center for p in self.ranging_points],
                'timestamp': plt.datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Save to file
            import json
            filename = f"uwb_data_{plt.datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            self._update_status(f"Data exported to {filename}")
        except Exception as e:
            self._update_status(f"Export failed: {str(e)}")

    def _update_std_dev(self, val):
        """Update standard deviation value from slider."""
        self.std_dev = val / 100.0  # Convert percentage to decimal
        
        # Update all ranging points with new std_dev
        for point in self.ranging_points:
            point.std_dev = self.std_dev
            point._update_range_visualization()
        
        # Update intersection and GDOP
        self._update_intersection()
        self._update_gdop()
        
        self._update_status(f"Error level set to {val}%")
        plt.draw()

    def _add_ranging_point(self):
        """Add a new ranging point at a random position."""
        # Generate random position within plot limits
        pos_x = (np.random.random() - 0.5) * 16
        pos_y = (np.random.random() - 0.5) * 16
        
        # Create new ranging point
        new_point = RangingPoint(
            self.ax, 
            self.anchor_pos, 
            (pos_x, pos_y), 
            self.std_dev, 
            self._update_intersection,
            self._update_gdop,
            self._update_path
        )
        
        self.ranging_points.append(new_point)
        self.history_points.append((pos_x, pos_y))
        self._update_intersection()
        self._update_gdop()
        self._update_status(f"Added point {len(self.ranging_points)} at ({pos_x:.2f}, {pos_y:.2f})")

    def _update_path(self):
        """Update the visualization of the drone path."""
        # Remove previous path if it exists
        if self.path_line:
            self.path_line.remove()
            
        if len(self.ranging_points) < 2:
            return
            
        # Extract point coordinates
        points = np.array([p.center for p in self.ranging_points])
        
        # Draw the path line
        self.path_line = self.ax.plot(
            points[:, 0], points[:, 1], 
            'g-', alpha=0.7, linewidth=2, 
            label='Drone Path' if not self.path_line else ""
        )[0]
        
        # Update the legend if this is the first time
        if len(self.ranging_points) == 2:
            self.ax.legend(loc='upper right')

        # Calculate and display total path length
        total_distance = 0
        for i in range(len(points) - 1):
            total_distance += np.linalg.norm(points[i] - points[i+1])
            
        # Display path info if there are enough points
        if hasattr(self, 'path_info_text') and self.path_info_text:
            self.path_info_text.remove()
            
        self.path_info_text = self.ax.text(
            0.02, 0.92, 
            f"Path Length: {total_distance:.2f} units\nPoints: {len(self.ranging_points)}", 
            transform=self.ax.transAxes,
            verticalalignment='top',
            fontsize=10,
            bbox=dict(facecolor='white', alpha=0.7)
        )

    def _calculate_position_estimate(self, intersection):
        """Calculate estimated position from intersection area."""
        if intersection.is_empty:
            return None
            
        # Use centroid of intersection area as position estimate
        centroid = intersection.centroid
        accuracy = np.sqrt(intersection.area / np.pi)  # Approximate accuracy as circle radius
        
        return (centroid.x, centroid.y), accuracy

    def _on_key_press(self, event):
        """Handle keyboard events."""
        if event.key == 'ctrl+c':
            plt.close(self.fig)
        elif event.key == 'a':
            self._add_ranging_point_callback(event)
        elif event.key == 'c':
            self._clear_path_callback(event)

    def _update_status(self, message):
        """Update the status text in the visualization."""
        if hasattr(self, 'status_text') and self.status_text:
            self.status_text.set_text(message)

    def _update_intersection(self):
        """Update the intersection area of all ranging regions."""
        # Remove previous intersection visualization if it exists
        if isinstance(self.intersection_patch, list):
            for patch in self.intersection_patch:
                patch.remove()
        elif self.intersection_patch:
            self.intersection_patch.remove()
            
        # Remove accuracy circle if it exists
        if self.accuracy_circle:
            self.accuracy_circle.remove()
            self.accuracy_circle = None
            
        # Skip if we don't have any ranging points
        if not self.ranging_points:
            return
            
        # Calculate intersection of all ranging donuts
        intersection = self.ranging_points[0].donut
        for point in self.ranging_points[1:]:
            intersection = intersection.intersection(point.donut)
            
        # Visualize intersection if it exists
        if not intersection.is_empty:
            self.intersection_patch = self._plot_polygon_with_hole(
                intersection, facecolor='green', alpha=0.75
            )
            
            # Calculate position estimate and accuracy
            pos_estimate, accuracy = self._calculate_position_estimate(intersection)
            
            # Draw accuracy circle
            if pos_estimate:
                self.accuracy_circle = plt.Circle(
                    pos_estimate, accuracy,
                    color='red', fill=False, linestyle='--'
                )
                self.ax.add_patch(self.accuracy_circle)
            
            # Update intersection area display
            area = intersection.area
            if self.intersection_area_text:
                self.intersection_area_text.set_text(
                    f'Intersection Area: {area:.2f}\n'
                    f'Est. Position: ({pos_estimate[0]:.2f}, {pos_estimate[1]:.2f})\n'
                    f'Accuracy: ±{accuracy:.2f} units'
                )
            else:
                self.intersection_area_text = self.ax.text(
                    0.02, 0.85, 
                    f'Intersection Area: {area:.2f}\n'
                    f'Est. Position: ({pos_estimate[0]:.2f}, {pos_estimate[1]:.2f})\n'
                    f'Accuracy: ±{accuracy:.2f} units',
                    transform=self.ax.transAxes, 
                    verticalalignment='top',
                    fontsize=10,
                    bbox=dict(facecolor='white', alpha=0.7)
                )

    def _update_gdop(self):
        """Calculate and update Geometric Dilution of Precision (GDOP)."""
        gdop = self._calculate_gdop()
        
        if gdop is not None:
            # Color-code GDOP quality
            if gdop < 5:
                color = 'green'
                quality = 'Excellent'
            elif gdop < 10:
                color = 'blue'
                quality = 'Good'
            elif gdop < 20:
                color = 'orange'
                quality = 'Fair'
            else:
                color = 'red'
                quality = 'Poor'
                
            if self.gdop_text:
                self.gdop_text.set_text(f'GDOP: {gdop:.2f} ({quality})')
                self.gdop_text.set_color(color)
            else:
                self.gdop_text = self.ax.text(
                    0.02, 0.95, 
                    f'GDOP: {gdop:.2f} ({quality})', 
                    transform=self.ax.transAxes, 
                    verticalalignment='top',
                    fontsize=10,
                    color=color,
                    bbox=dict(facecolor='white', alpha=0.7)
                )

    def _calculate_gdop(self):
        """Calculate Geometric Dilution of Precision."""
        if len(self.ranging_points) < 2:
            return None  # Not enough points to calculate GDOP
            
        # Build matrix for GDOP calculation
        positions = np.array([point.center for point in self.ranging_points])
        A = []
        
        for pos in positions:
            x_i, y_i = pos
            x, y = self.anchor_pos
            R = np.sqrt((x_i - x)**2 + (y_i - y)**2)
            A.append([(x_i - x)/R, (y_i - y)/R, 1])
            
        A = np.array(A)
        
        try:
            # Calculate GDOP as sqrt(trace(inv(A^T * A)))
            inv_at_a = np.linalg.inv(A.T @ A)
            gdop = np.sqrt(np.trace(inv_at_a))
            return gdop 
        except np.linalg.LinAlgError:
            return None  # Matrix is singular, cannot compute GDOP

    def _plot_polygon_with_hole(self, polygon, **kwargs):
        """Create a matplotlib patch for a polygon with potential holes."""
        if polygon.geom_type == 'Polygon':
            path = self._path_from_polygon(polygon)
            patch = PathPatch(path, **kwargs)
            self.ax.add_patch(patch)
            return patch
        
        elif polygon.geom_type == 'MultiPolygon':
            patches = []
            for part in polygon.geoms:
                path = self._path_from_polygon(part)
                patch = PathPatch(path, **kwargs)
                self.ax.add_patch(patch)
                patches.append(patch)
            return patches
        
        return None

    @staticmethod
    def _path_from_polygon(polygon):
        """Convert a Shapely polygon to a matplotlib path."""
        # Create exterior path
        exterior_coords = polygon.exterior.coords.xy
        codes = [Path.MOVETO] + [Path.LINETO] * (len(exterior_coords[0]) - 2) + [Path.CLOSEPOLY]
        vertices = [(x, y) for x, y in zip(*exterior_coords)]
        
        # Add interior paths (holes)
        for interior in polygon.interiors:
            interior_coords = interior.coords.xy
            codes += [Path.MOVETO] + [Path.LINETO] * (len(interior_coords[0]) - 2) + [Path.CLOSEPOLY]
            vertices += [(x, y) for x, y in zip(*interior_coords)]
            
        path = Path(vertices, codes)
        return path

    def show(self):
        """Display the visualization."""
        plt.tight_layout()
        plt.show()


class RangingPoint:
    """Represents a UWB ranging point that can be interactively positioned."""
    
    # Class variable to track which point is being dragged
    _active_point = None
    
    def __init__(self, ax, anchor_pos, init_pos, std_dev, intersection_callback, gdop_callback, path_callback):
        """
        Initialize a ranging point.
        
        Args:
            ax: Matplotlib axis to draw on
            anchor_pos: Position of the anchor (reference point)
            init_pos: Initial position of this ranging point
            std_dev: Standard deviation for distance measurement
            intersection_callback: Function to call when updating intersection
            gdop_callback: Function to call when updating GDOP
            path_callback: Function to call when updating path
        """
        self.ax = ax
        self.anchor_pos = anchor_pos
        self.std_dev = std_dev
        self.intersection_callback = intersection_callback
        self.gdop_callback = gdop_callback
        self.path_callback = path_callback
        
        # Create draggable point visualization
        self.marker = plt.Circle(
            init_pos, 
            0.1, 
            color='blue', 
            alpha=0.8, 
            picker=True, 
            zorder=10
        )
        self.ax.add_patch(self.marker)
        
        # Initialize variables
        self.center = init_pos
        self.drag_data = None
        self.donut = None
        self.donut_patch = None
        
        # Connect event handlers
        self._connect_events()
        
        # Add text label with distance
        self.distance_label = self.ax.text(
            init_pos[0], init_pos[1] + 0.3, 
            f"{self._calculate_distance():.2f}", 
            ha='center',
            fontsize=8
        )
        
        # Initialize range visualization
        self._update_range_visualization()

    def _calculate_distance(self):
        """Calculate the distance from this point to the anchor."""
        return np.linalg.norm(np.array(self.center) - np.array(self.anchor_pos))

    def _connect_events(self):
        """Set up event handlers for interactivity."""
        self.cid_press = self.marker.figure.canvas.mpl_connect(
            'button_press_event', self._on_press
        )
        self.cid_release = self.marker.figure.canvas.mpl_connect(
            'button_release_event', self._on_release
        )
        self.cid_motion = self.marker.figure.canvas.mpl_connect(
            'motion_notify_event', self._on_motion
        )

    def _on_press(self, event):
        """Handle mouse button press events."""
        if event.inaxes != self.ax or RangingPoint._active_point is not None:
            return
            
        contains, _ = self.marker.contains(event)
        if not contains:
            return
            
        # Store initial press position for dragging
        self.drag_data = (self.marker.center, event.xdata, event.ydata)
        RangingPoint._active_point = self

    def _on_motion(self, event):
        """Handle mouse motion events for dragging."""
        if (self.drag_data is None or 
            RangingPoint._active_point is not self or 
            event.inaxes != self.ax):
            return
            
        # Calculate new position
        center, press_x, press_y = self.drag_data
        dx = event.xdata - press_x
        dy = event.ydata - press_y
        new_center = (center[0] + dx, center[1] + dy)
        
        # Update marker position
        self.marker.center = new_center
        self.center = new_center
        
        # Update distance label
        self.distance_label.set_position((new_center[0], new_center[1] + 0.3))
        self.distance_label.set_text(f"{self._calculate_distance():.2f}")
        
        # Update visualizations
        self._update_range_visualization()
        self.gdop_callback()
        self.intersection_callback()
        self.path_callback()
        
        # Redraw the figure
        self.marker.figure.canvas.draw_idle()

    def _on_release(self, event):
        """Handle mouse button release events."""
        if RangingPoint._active_point is not self:
            return
            
        # Reset drag data
        self.drag_data = None
        RangingPoint._active_point = None
        
        # Final redraw
        self.marker.figure.canvas.draw_idle()

    def _update_range_visualization(self):
        """Update the donut shape representing measurement range with error."""
        # Remove previous visualization if it exists
        if self.donut_patch is not None:
            if isinstance(self.donut_patch, list):
                for patch in self.donut_patch:
                    patch.remove()
            else:
                self.donut_patch.remove()
        
        # Calculate distance from anchor
        distance = self._calculate_distance()
        
        # Create outer and inner circles based on distance and standard deviation
        outer_radius = distance + distance * self.std_dev
        inner_radius = max(0, distance - distance * self.std_dev)
        
        # Create donut shape (outer circle minus inner circle)
        outer = Point(self.center).buffer(outer_radius)
        inner = Point(self.center).buffer(inner_radius)
        self.donut = outer.difference(inner)
        
        # Create visualization patch
        self.donut_patch = self._plot_polygon_with_hole(
            self.donut, 
            facecolor='blue', 
            alpha=0.3,
            edgecolor='blue',
            linewidth=1
        )
        
        # Draw a line from anchor to this point
        self._update_range_line()

    def _update_range_line(self):
        """Update the line from anchor to this point."""
        if hasattr(self, 'range_line') and self.range_line:
            self.range_line.remove()
            
        self.range_line = self.ax.plot(
            [self.anchor_pos[0], self.center[0]],
            [self.anchor_pos[1], self.center[1]],
            'k:', alpha=0.5
        )[0]

    def _plot_polygon_with_hole(self, polygon, **kwargs):
        """Create a matplotlib patch for a polygon with potential holes."""
        if polygon.geom_type == 'Polygon':
            path = self._path_from_polygon(polygon)
            patch = PathPatch(path, **kwargs)
            self.ax.add_patch(patch)
            return patch
        
        elif polygon.geom_type == 'MultiPolygon':
            patches = []
            for part in polygon.geoms:
                path = self._path_from_polygon(part)
                patch = PathPatch(path, **kwargs)
                self.ax.add_patch(patch)
                patches.append(patch)
            return patches
        
        return None

    @staticmethod
    def _path_from_polygon(polygon):
        """Convert a Shapely polygon to a matplotlib path."""
        # Create exterior path
        exterior_coords = polygon.exterior.coords.xy
        codes = [Path.MOVETO] + [Path.LINETO] * (len(exterior_coords[0]) - 2) + [Path.CLOSEPOLY]
        vertices = [(x, y) for x, y in zip(*exterior_coords)]
        
        # Add interior paths (holes)
        for interior in polygon.interiors:
            interior_coords = interior.coords.xy
            codes += [Path.MOVETO] + [Path.LINETO] * (len(interior_coords[0]) - 2) + [Path.CLOSEPOLY]
            vertices += [(x, y) for x, y in zip(*interior_coords)]
            
        path = Path(vertices, codes)
        return path


def main():
    """Main function to run the visualization."""
    viz = UWBVisualization()
    viz.show()


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Test Suite Runner for Drone UWB Anchor Initialization

This script discovers and runs all unit tests in the test directory.
It provides a convenient way to run the entire test suite with detailed reports.
"""

import unittest
import sys
import os
import time
import argparse
from typing import Optional, List, Tuple

def discover_and_run_tests(
    pattern: str = 'test_*.py',
    test_dir: Optional[str] = None,
    verbosity: int = 2,
    failfast: bool = False
) -> Tuple[unittest.TestResult, float]:
    """
    Discover and run all tests matching the pattern.
    
    Parameters:
    -----------
    pattern : str
        File pattern to match test files.
    test_dir : Optional[str]
        Directory containing tests. If None, use the current directory.
    verbosity : int
        Verbosity level for test output (1-3).
    failfast : bool
        If True, stop on first failure.
        
    Returns:
    --------
    Tuple[unittest.TestResult, float]
        Test result object and execution time in seconds.
    """
    # Use current directory if test_dir is not specified
    if test_dir is None:
        test_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Discover tests
    start_dir = os.path.abspath(test_dir)
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir, pattern=pattern)
    
    # Run tests
    start_time = time.time()
    runner = unittest.TextTestRunner(verbosity=verbosity, failfast=failfast)
    result = runner.run(suite)
    end_time = time.time()
    
    return result, end_time - start_time

def print_summary(result: unittest.TestResult, execution_time: float) -> None:
    """
    Print a summary of test results.
    
    Parameters:
    -----------
    result : unittest.TestResult
        Test result object.
    execution_time : float
        Time taken to execute tests in seconds.
    """
    print("\n" + "="*70)
    print(f"TEST SUMMARY")
    print("="*70)
    
    # Count tests
    total_tests = result.testsRun
    passed = total_tests - len(result.failures) - len(result.errors) - len(result.skipped)
    
    print(f"Total tests run: {total_tests}")
    print(f"Passed: {passed}")
    print(f"Failed: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")
    
    # Calculate success rate
    if total_tests > 0:
        success_rate = (passed / total_tests) * 100
        print(f"Success rate: {success_rate:.2f}%")
    
    print(f"Total execution time: {execution_time:.2f} seconds")
    print("="*70)
    
    # Print failures and errors if any
    if result.failures or result.errors:
        print("\nFAILURE AND ERROR DETAILS:")
        print("-"*70)
        
        if result.failures:
            print("\nFAILURES:")
            for i, (test, traceback) in enumerate(result.failures, 1):
                print(f"\n{i}. {test}")
                print(f"{traceback}")
        
        if result.errors:
            print("\nERRORS:")
            for i, (test, traceback) in enumerate(result.errors, 1):
                print(f"\n{i}. {test}")
                print(f"{traceback}")
    
    print("\n")

def main() -> int:
    """
    Main function to parse arguments and run tests.
    
    Returns:
    --------
    int
        Exit code (0 for success, 1 for failure).
    """
    parser = argparse.ArgumentParser(description="Run the UWB Anchor unit test suite")
    
    parser.add_argument(
        "--dir", "-d",
        help="Directory containing test files",
        default=None
    )
    
    parser.add_argument(
        "--pattern", "-p",
        help="File pattern for test discovery",
        default="test_*.py"
    )
    
    parser.add_argument(
        "--verbosity", "-v",
        help="Verbosity level (1-3)",
        type=int,
        choices=[1, 2, 3],
        default=2
    )
    
    parser.add_argument(
        "--failfast", "-f",
        help="Stop on first failure",
        action="store_true"
    )
    
    # Module specific options
    parser.add_argument(
        "--uwb-only",
        help="Run only UWB protocol tests",
        action="store_true"
    )
    
    parser.add_argument(
        "--dynamics-only",
        help="Run only drone dynamics tests",
        action="store_true"
    )
    
    parser.add_argument(
        "--simulator-only",
        help="Run only simulator tests",
        action="store_true"
    )
    
    args = parser.parse_args()
    
    # Determine test pattern based on module flags
    pattern = args.pattern
    if args.uwb_only:
        pattern = "test_*uwb*.py"
    elif args.dynamics_only:
        pattern = "test_*dynamics*.py"
    elif args.simulator_only:
        pattern = "test_*simulator*.py"
    
    # Run tests
    print(f"Running tests matching pattern: {pattern}")
    if args.dir:
        print(f"Test directory: {os.path.abspath(args.dir)}")
    
    result, execution_time = discover_and_run_tests(
        pattern=pattern,
        test_dir=args.dir,
        verbosity=args.verbosity,
        failfast=args.failfast
    )
    
    # Print summary
    print_summary(result, execution_time)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    sys.exit(main())
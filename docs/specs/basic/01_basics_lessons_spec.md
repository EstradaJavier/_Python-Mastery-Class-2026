# 01_basics.py Lesson Specification

## Overview

This document defines the lesson-level requirements and initial automated test design for `01_basics.py` in the Python Mastery 2026 project. The lesson introduces beginner Python foundations such as printed output, variables, basic data types, arithmetic, strings, booleans, simple functions, conditionals, lists, loops, and beginner self-testing patterns. The specification is aligned to the Basic lesson group requirements and follows a lightweight interpretation of ISO/IEC/IEEE 29148 for requirements structure and ISO/IEC/IEEE 29119 for test design traceability.[1][2][3][4]

The testing approach uses pytest with Jasmine-like behavioral logic: each question checks a clear behavior, may include a small parametrized set, and should produce learner-friendly feedback. Research on mastery-oriented educational assessment supports clear criteria, actionable feedback, and iterative improvement, which aligns with the agreed 8/10 lesson pass threshold for this project.[5][6][7][8][9][10]

## Scope

This specification covers automated assessment targets that are appropriate for Lesson 1. For this lesson, function return values are the primary testing surface, while printed output is tested only where the lesson explicitly teaches output behavior or where the output is a core learning objective.[11][12]

The following functions are in scope for automated testing:
- `calculate_age_from_dob(dob)`
- `create_profile(use_input=False)`
- `run_operations(age, height_meters)`
- `show_intro()`
- `visual_map()`
- `assert_fail_examples()`
- `self_test(name, age, height_meters, years_to_retirement)`

The following areas are initially out of scope for strict automated checking in this first draft:
- Stylistic comments and prose quality.
- IntelliJ usage notes.
- Freeform experimentation prompts.

## Lesson objectives

| Objective ID | Objective | Assessment focus |
|---|---|---|
| BASIC-OBJ-01-001 | Explain and demonstrate basic printed program output. | Console output presence and key phrases.[11][12] |
| BASIC-OBJ-01-002 | Use functions to organize beginner Python code. | Function availability and callable behavior. |
| BASIC-OBJ-01-003 | Calculate age from a date of birth. | Correct return value and integer type. |
| BASIC-OBJ-01-004 | Build and return a structured beginner profile. | Tuple structure, field values, and field types. |
| BASIC-OBJ-01-005 | Perform basic arithmetic operations and return computed results. | Deterministic numeric return values. |
| BASIC-OBJ-01-006 | Use assertions and interpret passing versus failing checks. | Successful self-test behavior and controlled assertion-failure examples.[13] |

## Requirements

- **BASIC-01-REQ-001**: `calculate_age_from_dob(dob)` shall return the age in whole years as an integer for a valid `date` input.
- **BASIC-01-REQ-002**: `calculate_age_from_dob(dob)` shall correctly account for whether the birthday has already occurred in the current year.
- **BASIC-01-REQ-003**: `create_profile(use_input=False)` shall return a tuple containing exactly 10 values in the documented order.
- **BASIC-01-REQ-004**: When `use_input=False`, `create_profile()` shall use the lesson’s default date of birth and compute age from that date.
- **BASIC-01-REQ-005**: `create_profile()` shall compute height in meters as a rounded float value based on 5 feet 10 inches.
- **BASIC-01-REQ-006**: `run_operations(age, height_meters)` shall return a tuple of `(years_to_retirement, height_feet_decimal)` using the documented formulas.
- **BASIC-01-REQ-007**: `self_test(...)` shall complete without raising an exception when provided valid values that satisfy the lesson assertions.
- **BASIC-01-REQ-008**: `assert_fail_examples()` shall demonstrate assertion failures in a controlled way without terminating the lesson program, using `try/except` blocks around intentional failures.
- **BASIC-01-REQ-009**: `show_intro()` shall print an introduction containing the lesson identity and beginner Python foundations.[11][12]
- **BASIC-01-REQ-010**: `visual_map()` shall print the intended high-level program flow and include `main()` and core called functions.[11][12]

## Assessment questions

The lesson shall be assessed using 10 questions. Each question may include a small parametrized set where appropriate.[5][6]

| Question ID | Requirement mapping | Type | Pass condition |
|---|---|---|---|
| BASIC-01-Q-001 | REQ-001, REQ-002 | Core correctness | Returns correct integer age for representative DOB cases. |
| BASIC-01-Q-002 | REQ-001, REQ-002 | Edge case | Correctly handles birthday-not-yet-occurred logic. |
| BASIC-01-Q-003 | REQ-003, REQ-004 | Core correctness | `create_profile(False)` returns a 10-item tuple in the documented order. |
| BASIC-01-Q-004 | REQ-005 | Type/format | Height in meters is a float rounded to two decimals and equals 1.78 for the default profile. |
| BASIC-01-Q-005 | REQ-003 | Core correctness | Returned profile field types match beginner expectations, such as `str`, `int`, `bool`, and `date`. |
| BASIC-01-Q-006 | REQ-006 | Core correctness | `run_operations()` returns correct retirement and height-feet-decimal values. |
| BASIC-01-Q-007 | REQ-007 | Positive behavior | `self_test()` passes silently for valid inputs. |
| BASIC-01-Q-008 | REQ-008 | Output/behavior | `assert_fail_examples()` prints controlled assertion-failure explanations without raising to the caller.[11][12] |
| BASIC-01-Q-009 | REQ-009 | Output/behavior | `show_intro()` prints required introductory phrases.[11][12] |
| BASIC-01-Q-010 | REQ-010 | Output/behavior | `visual_map()` prints the expected high-level flow labels.[11][12] |

A learner passes the lesson when at least 8 of 10 questions pass, consistent with the Basic lesson group mastery policy supported by mastery-learning guidance.[7][14][9]

## Pytest design guidance

The initial pytest implementation should use `@pytest.mark.parametrize` for deterministic data-driven checks, especially for age calculation and arithmetic behavior.[5][6] Console-output verification should use pytest output-capture support only for the functions whose learning objective explicitly includes printed output.[11][12]

Recommended conventions:
- File name: `tests/basic/test_01_basics.py`
- Friendly test names such as `test_calculate_age_from_dob_returns_expected_years`
- Helper fixtures only if they reduce repetition and remain beginner-readable
- Failure messages phrased to teach the concept rather than only report a mismatch.[8][10]

## Traceability

| Requirement ID | Question ID | Planned test function |
|---|---|---|
| BASIC-01-REQ-001 | BASIC-01-Q-001 | `test_calculate_age_from_dob_returns_expected_years` |
| BASIC-01-REQ-002 | BASIC-01-Q-002 | `test_calculate_age_from_dob_handles_pre_birthday_case` |
| BASIC-01-REQ-003 | BASIC-01-Q-003 | `test_create_profile_returns_documented_tuple_shape` |
| BASIC-01-REQ-005 | BASIC-01-Q-004 | `test_create_profile_returns_expected_height_meters` |
| BASIC-01-REQ-006 | BASIC-01-Q-006 | `test_run_operations_returns_expected_values` |
| BASIC-01-REQ-007 | BASIC-01-Q-007 | `test_self_test_accepts_valid_values` |
| BASIC-01-REQ-008 | BASIC-01-Q-008 | `test_assert_fail_examples_prints_explanations_without_raising` |
| BASIC-01-REQ-009 | BASIC-01-Q-009 | `test_show_intro_prints_expected_headings` |
| BASIC-01-REQ-010 | BASIC-01-Q-010 | `test_visual_map_prints_program_flow` |

## Risks and notes

The lesson currently mixes instructional output and testable logic in one file, which is acceptable for an early beginner lesson but may become harder to test as lessons grow. Pytest can still support this style effectively, but long-term maintainability will improve if future lessons keep core logic return-value-oriented and reserve printed output for explicit teaching moments.[5][6][11]

The `self_test()` function currently calls `assert_fail_examples()` before its own assertions, which means automated tests for `self_test()` may also capture printed failure examples as part of normal execution. That is not necessarily wrong for the lesson, but it is a design choice worth revisiting if cleaner separation between passing checks and intentional failure demonstrations is desired.
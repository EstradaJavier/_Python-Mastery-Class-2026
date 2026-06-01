# Basic Lesson Group Requirements Specification

## Purpose

This document defines the requirements, assessment model, and initial test design direction for the **Basic** lesson group in the `javiere-python-mastery-class-2026` repository. The goal is to support beginner-friendly Python learning through behavior-based automated testing implemented with pytest, using a Jasmine-like pass/fail style with parametrized input sets where appropriate.[cite:41][cite:42][cite:77]

The specification follows the spirit of ISO/IEC/IEEE 29148 for requirements engineering and ISO/IEC/IEEE 29119 for test documentation and design, while remaining lightweight enough for an educational repository.[cite:56][cite:57][cite:64][cite:67]

## Scope

The Basic lesson group covers introductory Python concepts, with assessment focused primarily on function return values during the early learning stages. Console output should only be tested when a lesson explicitly teaches output behavior or when output is a stated part of the exercise objective.[cite:62][cite:65]

This specification applies to:
- Basic lesson requirements.
- Basic lesson assessment behavior.
- Pytest test design conventions for the Basic lesson group.
- Traceability between lesson objectives and automated tests.[cite:57][cite:64]

This specification does not yet define Intermediate, Advanced, or Additional lesson requirements.

## Assessment philosophy

The Basic lesson group uses a mastery-oriented assessment model. Research on mastery learning and mastery grading supports clear objectives, pass/fail or mastery-style checks, actionable feedback, and opportunities to improve after initial failure rather than relying only on one-shot, high-stakes binary outcomes.[cite:71][cite:75][cite:78][cite:84]

For this project, the standard shall be:
- Each question is graded as pass/fail.
- Each question may use a small parametrized set of inputs and expected outputs.
- A lesson passes when the learner achieves **8 out of 10** questions correct.
- Failed lessons should present a smaller, learner-friendly set of failing cases and actionable guidance rather than an overwhelming dump of every possible error.[cite:41][cite:42][cite:76][cite:82]

## Testing style

The testing style shall follow a Jasmine-like behavioral model, implemented in pytest. This means tests should describe expected behavior in plain language, validate both passing and failing examples, and remain highly readable for beginners.[cite:41][cite:42][cite:77][cite:83]

The preferred pytest techniques for this lesson group are:
- `@pytest.mark.parametrize` for grouped pass/fail examples.[cite:41][cite:42]
- Direct assertions for return values.[cite:46]
- Output capture only when required by the lesson objective, using pytest output-capture features when needed.[cite:62][cite:65]
- Friendly test names and failure messages that reinforce the lesson objective.[cite:76][cite:82]

## Requirements

### Functional requirements

- **BASIC-REQ-001**: Each Basic lesson shall define up to 10 assessment questions aligned to explicit lesson objectives.
- **BASIC-REQ-002**: Each assessment question may include a small parametrized input set instead of a single example, where doing so improves behavioral coverage without overwhelming the learner.[cite:41][cite:42]
- **BASIC-REQ-003**: Early Basic lessons shall prioritize testing function return values rather than console interaction, unless console output is an explicit learning objective.[cite:62][cite:65]
- **BASIC-REQ-004**: Each lesson shall use standardized function names or explicitly documented callable entry points so automated tests can evaluate learner solutions consistently.[cite:47][cite:53]
- **BASIC-REQ-005**: Each question shall test one primary behavior only.
- **BASIC-REQ-006**: Each lesson shall be considered passing when at least 8 of 10 questions pass.
- **BASIC-REQ-007**: Each failing question shall produce learner-friendly feedback that identifies the missed concept or behavior.
- **BASIC-REQ-008**: Tests shall cover positive cases, negative cases, and edge cases when appropriate to the lesson objective.[cite:46][cite:53]

### Documentation requirements

- **BASIC-REQ-009**: Each lesson shall have a traceable mapping between lesson objective, question ID, and automated test implementation.[cite:57][cite:64]
- **BASIC-REQ-010**: Each test module shall contain clear naming that indicates the behavior being tested.[cite:47][cite:53]
- **BASIC-REQ-011**: Each lesson spec shall document whether output capture, exception handling, or pure return-value testing is in scope.[cite:62][cite:65]

## Question model

Each Basic lesson question should fit one of the following patterns:

1. **Core correctness**: verifies the expected result for standard inputs.
2. **Negative behavior**: verifies that a near-miss or invalid case does not incorrectly pass.
3. **Boundary or edge behavior**: verifies zero, empty input, case sensitivity, or similar lesson-relevant boundaries.
4. **Type or format behavior**: verifies that the learner returns the right type or format when the lesson objective requires it.[cite:46][cite:53]

A recommended 10-question distribution for Basic lessons is:
- 4 core correctness questions.
- 2 negative-behavior questions.
- 2 edge or boundary questions.
- 1 type/format question.
- 1 lesson-specific comprehension question.[cite:46][cite:53]

## Human factors guidance

Educational assessment should support learning, confidence, and correction. Research on assessment and mastery-based learning indicates that learners benefit from aligned objectives, actionable feedback, and iterative opportunities to improve rather than purely punitive failure models.[cite:76][cite:78][cite:84]

For that reason, the Basic lesson group should follow these human-factor principles:
- Show a smaller, digestible set of failures first.[cite:82]
- Phrase feedback in concept language, such as “This function should return `True` for even numbers,” instead of only raw assertion output.[cite:76][cite:82]
- Avoid mixing multiple concepts into one question.
- Keep tests deterministic and stable so learners can trust the results.[cite:53]

## Traceability model

Each lesson should map objectives to tests using simple IDs, such as:

| Lesson objective ID | Question ID | Test file | Test function pattern |
|---|---|---|---|
| BASIC-OBJ-001 | BASIC-Q-001 | `tests/basic/test_<lesson>.py` | `test_<behavior>_...` |
| BASIC-OBJ-002 | BASIC-Q-002 | `tests/basic/test_<lesson>.py` | `test_<behavior>_...` |
| BASIC-OBJ-003 | BASIC-Q-003 | `tests/basic/test_<lesson>.py` | `test_<behavior>_...` |

This approach supports traceability recommended by formal requirements and test-documentation practices without making the repository too heavy for educational use.[cite:57][cite:64]

## Directory structure

The following directories should exist in the repository to support the planned workflow:

```text
docs/specs/basic/
docs/specs/intermediate/
docs/specs/advanced/
docs/specs/additional/
tests/basic/
tests/intermediate/
tests/advanced/
tests/additional/
tests/shared/
```

## Initial implementation guidance

The first implementation steps for the Basic lesson group should be:
- Create one master Basic lesson group requirements specification.
- Create one detailed lesson-level spec for the first Basic lesson.
- Create one pytest module for that first Basic lesson in `tests/basic/`.
- Implement parametrized tests for return-value behavior first.[cite:41][cite:42]
- Introduce output-capture assertions only for lessons that explicitly teach output behavior.[cite:62][cite:65]

## Approval criteria

This Basic lesson group specification should be considered approved for use when:
- The directory structure exists in the repository.
- The Basic lesson group document is stored under `docs/specs/basic/`.
- The first lesson-level spec is drafted.
- The first pytest module is created using the conventions defined here.
- Requirement IDs and question IDs are used consistently in future lesson specs.[cite:57][cite:64]

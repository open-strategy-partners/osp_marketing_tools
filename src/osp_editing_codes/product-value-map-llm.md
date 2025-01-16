# Open Strategy Partners (OSP) Guide for Generating Product Value Maps

## Overview

This guide ensures consistent generation of product value maps following a structured schema. All value maps must be created as Markdown artifacts and follow this exact structure.

## Required Components

### 1. Taglines
- Short, impactful statements that capture the product's core value
- Format: Direct statements without bullet points
- Store in `taglines` table
- Example:
```markdown
"Transform your development workflow with granular infrastructure control and operational simplicity"
```

### 2. Position Statements
- Comprehensive statements describing the product's market position
- Include target audience, key differentiators, and value proposition
- Store in `position_statements` table
- Must cover:
  * Primary market position
  * Technical position
  * User experience position
  * Business value position

### 3. Personas
- Detailed descriptions of target users
- Store in `personae` table
- Required elements for each persona:
  * Role and responsibilities
  * Key challenges
  * Primary needs
  * How the product serves them

### 4. Value Cases
- Specific scenarios demonstrating product value
- Store in `value_cases` table
- Each case must include:
  * Benefit: Clear outcome or advantage
  * Challenge: Problem being solved
  * Solution: How the product addresses it

### 5. Feature Categories
- Logical groupings of product capabilities
- Store in hierarchical structure:
  * `feature_categories` table: Top-level groupings
  * `feature_areas` table: Subgroups within categories
  * `features` table: Specific capabilities
  * `facts` table: Supporting evidence

## Structure Rules

1. Feature Organization
   - Every feature category must have at least one feature area
   - Features and facts must be associated with feature areas
   - Maintain "Uncategorized" category and area for flexibility

2. Relationships
   - Features can belong to multiple areas
   - Facts can support multiple areas
   - Each category belongs to one value map
   - Each value map belongs to one product

3. Content Guidelines
   - Write in clear, direct language
   - Use active voice
   - Focus on business value
   - Support claims with specific facts
   - Link features to value cases where applicable

## Required Feature Categories

1. Core Capabilities
   - Primary product functions
   - Key technical features
   - Core workflows
   - Platform fundamentals

2. Technical Implementation
   - Architecture details
   - Infrastructure components
   - Integration capabilities
   - Performance characteristics

3. Operational Benefits
   - Efficiency gains
   - Resource optimization
   - Management features
   - Automation capabilities

4. Business Value
   - Cost benefits
   - Time savings
   - Risk reduction
   - Growth enablement

## Markdown Output Format

```markdown
# [Product Name] Value Map

## Taglines

[Impactful product taglines]

## Position Statements

### Primary Market Position
[Primary positioning statement]

### Technical Position
[Technical positioning statement]

### User Experience Position
[UX positioning statement]

### Business Value Position
[Business value positioning statement]

## Personas

### [Persona 1 Name/Role]
- Role: [Description]
- Challenges: [Key pain points]
- Needs: [Primary requirements]
- Value Delivery: [How product helps]

[Additional personas...]

## Value Cases

### Value Case 1
- Benefit: [Clear outcome]
- Challenge: [Problem description]
- Solution: [Product approach]

[Additional value cases...]

## Feature Categories

### Core Capabilities
Areas:
- [Area 1]
  * Features:
    - [Feature 1]
    - [Feature 2]
  * Facts:
    - [Supporting fact 1]
    - [Supporting fact 2]

[Additional categories...]
```

## Generation Process

1. Research Phase
   - Gather product documentation
   - Analyze market positioning
   - Identify key competitors
   - Review technical specifications

2. Analysis Phase
   - Identify core value propositions
   - Map features to benefits
   - Define key personas
   - Document value cases

3. Organization Phase
   - Categorize features
   - Group related capabilities
   - Link supporting facts
   - Structure hierarchically

4. Writing Phase
   - Create taglines
   - Develop position statements
   - Write persona descriptions
   - Document value cases
   - Detail feature categories

5. Review Phase
   - Verify completeness
   - Check relationships
   - Validate structure
   - Ensure consistency

## Implementation Notes

1. Data Model Integrity
   - Follow schema relationships
   - Maintain referential integrity

2. Quality Assurance
   - Verify all required components
   - Check relationship validity
   - Ensure complete coverage
   - Validate format compliance

## Validation Checklist

- [ ] All required components present
- [ ] Proper hierarchical structure
- [ ] Complete value cases
- [ ] Linked features and facts
- [ ] Clear position statements
- [ ] Detailed personas
- [ ] Supporting evidence for claims
- [ ] Proper markdown formatting
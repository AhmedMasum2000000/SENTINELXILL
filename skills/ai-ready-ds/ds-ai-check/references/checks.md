# Check Definitions

Every check is deterministic. Apply each rule to the extracted Figma data and record PASS / PARTIAL / FAIL with the exact counts.

---

## Category 1: Token Architecture

**Data source:** `get_variable_defs` output (variable collections, variables, modes)

### T1 — Variable Collections Exist
- **PASS**: At least 1 variable collection exists
- **FAIL**: No variable collections found
- **Weight**: 10

### T2 — Multi-Layer Hierarchy
- **PASS**: 3+ collections exist with names suggesting layers (look for: primitive/base/core, semantic/theme/alias, component/specific)
- **PARTIAL**: 2 collections exist
- **FAIL**: 0-1 collections
- **How to detect layers**: Match collection names (case-insensitive) against these keyword groups:
  - Primitive layer: `primitive`, `base`, `core`, `raw`, `global`, `foundation`
  - Semantic layer: `semantic`, `theme`, `alias`, `purpose`, `token`, `system`
  - Component layer: `component`, `specific`, `local`, `override`
- **Weight**: 20

### T3 — Semantic Naming Convention
- **Rule**: For each variable, check if the name follows a multi-segment pattern with meaningful segments (contains at least 2 separators: `/`, `-`, or `.`)
- **PASS**: 80%+ of variables use multi-segment names
- **PARTIAL**: 40-79%
- **FAIL**: Below 40%
- **Examples**:
  - GOOD: `color/action/primary/default`, `spacing-md`, `text.heading.lg`
  - BAD: `blue500`, `16px`, `myColor`, `var1`
- **Weight**: 20

### T4 — Variable Description Coverage
- **Rule**: Count variables that have a non-empty `description` field
- **PASS**: 60%+ have descriptions
- **PARTIAL**: 20-59%
- **FAIL**: Below 20%
- **Weight**: 15

### T5 — Variable Type Diversity
- **Rule**: Check that variables span multiple types (COLOR, FLOAT, STRING, BOOLEAN)
- **PASS**: 3+ types used
- **PARTIAL**: 2 types
- **FAIL**: 1 type only
- **Weight**: 10

### T6 — Mode Support
- **Rule**: Check if any collection has multiple modes (light/dark, brand variants, density)
- **PASS**: At least 1 collection has 2+ modes
- **FAIL**: All collections single-mode
- **Weight**: 10

### T7 — Variable Aliasing (References)
- **Rule**: Check if variables reference other variables (alias chains = token hierarchy in action)
- **PASS**: 30%+ of variables are aliases
- **PARTIAL**: 10-29%
- **FAIL**: Below 10% or can't detect
- **Weight**: 15

---

## Category 2: Component Contracts

**Data source:** `get_design_context` output (components, properties, variants)

### C1 — Components Exist
- **PASS**: 10+ components/component sets defined
- **PARTIAL**: 1-9 components
- **FAIL**: 0 components
- **Weight**: 10

### C2 — Component Description Coverage
- **Rule**: Count components that have a non-empty `description`
- **PASS**: 70%+ have descriptions
- **PARTIAL**: 30-69%
- **FAIL**: Below 30%
- **Weight**: 20

### C3 — Variant Coverage
- **Rule**: Count component sets (components with variants) vs standalone components
- **PASS**: 60%+ of components are part of component sets (have variants)
- **PARTIAL**: 30-59%
- **FAIL**: Below 30%
- **Weight**: 20

### C4 — Property Definitions
- **Rule**: Count components that expose explicit properties (boolean, text, instance-swap, variant)
- **PASS**: 70%+ of components have defined properties
- **PARTIAL**: 30-69%
- **FAIL**: Below 30%
- **Weight**: 20

### C5 — Naming Consistency
- **Rule**: Check component names follow a consistent convention:
  - All use PascalCase, or all use kebab-case, or all use a clear prefix pattern
  - Detect the dominant pattern and measure adherence
- **PASS**: 80%+ follow the dominant pattern
- **PARTIAL**: 50-79%
- **FAIL**: Below 50%
- **Weight**: 15

### C6 — State Completeness
- **Rule**: For components with variants, check if common states are represented (default, hover, active, disabled, focus)
- **PASS**: 50%+ of variant components include 3+ states
- **PARTIAL**: 25-49%
- **FAIL**: Below 25%
- **How to detect**: Look for variant property values containing: `default`, `hover`, `active`, `pressed`, `disabled`, `focus`, `selected`, `error`, `loading`
- **Weight**: 15

---

## Category 3: Design-Code Parity

**Data source:** `get_code_connect_map` output

### P1 — Code Connect Exists
- **PASS**: At least 1 Code Connect mapping exists
- **FAIL**: No Code Connect mappings found
- **Weight**: 40

### P2 — Mapping Coverage
- **Rule**: Count mapped components vs total components (from design context)
- **PASS**: 60%+ of components have Code Connect mappings
- **PARTIAL**: 20-59%
- **FAIL**: Below 20%
- **Weight**: 35

### P3 — Naming Alignment
- **Rule**: For mapped components, check if Figma component name can be derived from code component name (case-insensitive, ignoring separators)
- **PASS**: 80%+ of mappings have aligned names
- **PARTIAL**: 50-79%
- **FAIL**: Below 50%
- **Weight**: 25

---

## Category 4: Accessibility Readiness

**Data source:** `get_variable_defs` (for color tokens), `get_design_context` (for component patterns)

### A1 — Color Token Coverage
- **Rule**: Check what percentage of color-type variables use semantic names suggesting purpose (not raw color names)
- **PASS**: 70%+ of color variables have semantic names (contain: `action`, `text`, `background`, `surface`, `border`, `error`, `warning`, `success`, `info`, `on-`, `fg`, `bg`)
- **PARTIAL**: 30-69%
- **FAIL**: Below 30%
- **Weight**: 25

### A2 — State Indication Beyond Color
- **Rule**: Check if components with states (error, disabled, active) use non-color indicators — look for variant properties suggesting icons, borders, or text changes alongside color
- **PASS**: Evidence of non-color state indicators in 50%+ of stateful components
- **PARTIAL**: 20-49%
- **FAIL**: Below 20% or can't detect
- **Weight**: 25

### A3 — Contrast-Friendly Token Pairs
- **Rule**: Check for paired token patterns (e.g., `background` + `on-background`, `surface` + `on-surface`, `action` + `on-action`)
- **PASS**: 3+ paired token patterns found
- **PARTIAL**: 1-2 pairs
- **FAIL**: No pairs detected
- **How to detect**: Look for variable names where one contains `bg`/`background`/`surface` and a sibling contains `on-`/`fg`/`text` + the same suffix
- **Weight**: 25

### A4 — Focus State Tokens
- **Rule**: Check for variables whose names suggest focus styling (`focus`, `outline`, `ring`)
- **PASS**: Focus-related variables exist (2+)
- **PARTIAL**: 1 focus variable
- **FAIL**: None found
- **Weight**: 25

---

## Category 5: Documentation Quality

**Data source:** `get_design_context`, `get_variable_defs`, `get_metadata`

### D1 — File-Level Organization
- **Rule**: Check if the file has multiple pages with meaningful names (not just "Page 1")
- **PASS**: 3+ pages with descriptive names
- **PARTIAL**: 2 pages or pages with generic names
- **FAIL**: 1 page only
- **Weight**: 15

### D2 — Component Descriptions (reuses C2 data)
- **Rule**: Same as C2 — percentage of components with descriptions
- **PASS**: 70%+
- **PARTIAL**: 30-69%
- **FAIL**: Below 30%
- **Weight**: 30

### D3 — Variable Descriptions (reuses T4 data)
- **Rule**: Same as T4 — percentage of variables with descriptions
- **PASS**: 60%+
- **PARTIAL**: 20-59%
- **FAIL**: Below 20%
- **Weight**: 30

### D4 — Usage Guidelines Signals
- **Rule**: Check component descriptions for actionable content — look for descriptions longer than 20 characters that contain guidance words (`use`, `when`, `don't`, `avoid`, `instead`, `for`, `should`, `must`, `note`)
- **PASS**: 40%+ of descriptions contain guidance
- **PARTIAL**: 15-39%
- **FAIL**: Below 15%
- **Weight**: 25

---

## Category 6: Governance & Maintenance

**Data source:** `get_design_context`, `get_variable_defs`, `get_metadata`

### G1 — Deprecation Signals
- **Rule**: Check for components or variables with names or descriptions containing deprecation markers (`deprecated`, `legacy`, `old`, `do not use`, `obsolete`, `[deprecated]`)
- **PASS**: Deprecation markers found AND those items have descriptions explaining the replacement
- **PARTIAL**: Deprecation markers found but no replacement guidance
- **FAIL**: No deprecation signals (neutral — could mean nothing is deprecated or they aren't tracked)
- **Note**: Score FAIL as 50/100 (neutral) since absence could be legitimate
- **Weight**: 20

### G2 — Consistent Naming Taxonomy
- **Rule**: Check if variable collections and component names follow a common taxonomy (shared prefixes, consistent separators, organized grouping)
- **PASS**: 80%+ of variables share a common prefix/grouping pattern within their collection
- **PARTIAL**: 50-79%
- **FAIL**: Below 50%
- **Weight**: 30

### G3 — Component Organization
- **Rule**: Check if components are organized in a hierarchical structure (using `/` in names for grouping, e.g., `Button/Primary`, `Form/Input`)
- **PASS**: 60%+ of components use hierarchical naming
- **PARTIAL**: 30-59%
- **FAIL**: Below 30%
- **Weight**: 25

### G4 — System Completeness
- **Rule**: Check for presence of foundational token categories: color, spacing, typography (font-size/line-height/font-weight), border-radius, shadows/elevation
- **PASS**: 4+ categories present
- **PARTIAL**: 2-3 categories
- **FAIL**: 0-1 categories
- **How to detect**: Match variable names/groups against category keywords:
  - Color: `color`, `colour`, `fill`, `stroke`, `bg`, `fg`
  - Spacing: `space`, `spacing`, `gap`, `margin`, `padding`, `size`
  - Typography: `font`, `text`, `type`, `line-height`, `letter-spacing`, `weight`
  - Radius: `radius`, `corner`, `rounded`, `border-radius`
  - Shadow/Elevation: `shadow`, `elevation`, `depth`, `blur`, `spread`
- **Weight**: 25

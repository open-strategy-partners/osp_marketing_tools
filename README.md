# Open Strategy Partners (OSP) Marketing Tools for LLMs

A comprehensive suite of tools for technical content creation, optimization, and product positioning based on [Open Strategy Partners](https://openstrategypartners.com)' proven methodologies. This software is based on the [Model Context Protocol (MCP)](https://openstrategypartners.com/blog/the-model-context-protocol-unify-your-marketing-stack-with-ai/) and is to be used by any LLM client that supports the MCP.

![](https://badge.mcpx.dev?type=server 'MCP Server') 

## Features

### 1. OSP Product Value Map Generator
Generate structured [OSP product value maps](https://openstrategypartners.com/the-osp-value-map/) that effectively communicate your product's worth and positioning:
- Tagline creation and refinement
- Position statements across market, technical, UX, and business dimensions
- Persona development with roles, challenges, and needs
- Value case documentation
- Feature categorization and organization
- Hierarchical structure for features, areas, and categories
- Validation system for completeness and consistency

### 2. OSP Meta Information Generator
Create optimized metadata for web content:
- Article titles (H1) with proper keyword placement
- Meta titles optimized for search (50-60 characters)
- Meta descriptions with clear value propositions (155-160 characters)
- SEO-friendly URL slugs
- Search intent analysis
- Mobile display optimization
- Click-through rate enhancement suggestions

### 3. OSP Content Editing Codes
Apply [OSP's semantic editing codes](https://openstrategypartners.com/resources/the-osp-editing-codes/) for comprehensive content review:
- Scope and narrative structure analysis
- Flow and readability enhancement
- Style and phrasing optimization
- Word choice and grammar verification
- Technical accuracy validation
- Inclusive language guidance
- Constructive feedback generation with before/after examples

### 4. OSP Technical Writing Guide
Systematic approach to creating high-quality technical content:
- Narrative structure development
- Flow optimization
- Style guidelines
- Technical accuracy verification
- Content type-specific guidance (tutorials, reference docs, API documentation)
- Accessibility considerations
- Internationalization best practices
- Quality assurance checklists

## Usage Examples

In all of these examples, it is assumed that you will provide the texts that you wish to improve, or the technical documentation that describes the product you are marketing. 

### Value Map Generation

```plaintext
Prompt: "Generate an OSP value map for [Product Name] focusing on [target audience] with the following key features: [list features]"

Example:
"Generate an OSP value map for CloudDeploy, focusing on DevOps engineers with these key features:
- Automated deployment pipeline
- Infrastructure as code support
- Real-time monitoring
- Multi-cloud compatibility
- [the rest of your features or text]"
```

### Meta Information Creation

```plaintext
Prompt: "Use the OSP meta tool to generate metadata for an article about [topic]. Primary keyword: [keyword], audience: [target audience], content type: [type]"

Example:
"Use the OSP meta tool to generate metadata for an article about containerization best practices. Primary keyword: 'Docker containers', audience: system administrators, content type: technical guide"
```

### Content Editing

```plaintext
Prompt: "Review this technical content using OSP editing codes: [paste content]"

Example:
"Review this technical content using OSP editing codes:
Kubernetes helps you manage containers. It's really good at what it does. You can use it to deploy your apps and make them run better."
```

### Technical Writing

```plaintext
Prompt: "Apply the OSP writing guide to create a [document type] about [topic] for [audience]"

Example:
"Apply the OSP writing guide to create a tutorial about setting up a CI/CD pipeline for junior developers"
```

## Requirements

- Python must be installed on your system
- `uv` Python package installer must be installed
    - Installation instructions for `uv` can be found at [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

## Configuration

Add the following to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "osp_marketing_tools": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/open-strategy-partners/osp_marketing_tools@main",
                "osp-marketing-tools"
            ]
        }
    }
}
```

## Integration

The software can be integrated into your content workflow through:
- API endpoints
- Command-line interface
- Web interface
- Content management system plugins

## Attribution

This software package implements the content creation and optimization methodologies developed by [Open Strategy Partners](https://openstrategypartners.com). It is based on their LLM-enabled marketing tools and professional content creation frameworks.

For more information and original resources, visit:
1. [The OSP Writing and Editing Guide](https://openstrategypartners.com/osp-writing-editing-guide/)
2. [Editing Codes Quickstart Guide](https://openstrategypartners.com/blog/osp-editing-codes-quick-start-guide/)
3. [OSP Free Resources](https://openstrategypartners.com/resources/)

## License

This software is licensed under the Attribution-ShareAlike 4.0 International license from Creative Commons Corporation ("Creative Commons"). 

This means you are free to:
- Share: Copy and redistribute the material in any medium or format
- Adapt: Remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- Attribution: You must give appropriate credit to Open Strategy Partners, provide a link to the license, and indicate if changes were made
- ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original

For the full license text, visit: [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/)

## Contributing

We welcome contributions to improve these tools. Please submit issues and pull requests through our repository.

## Support

For questions and support:
1. Check our documentation
2. Submit an issue in our repository
3. Contact Open Strategy Partners for professional consulting

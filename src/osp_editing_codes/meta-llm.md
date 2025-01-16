# LLM Prompting Guide for Meta Information Creation

This guide provides instructions for prompting Language Learning Models (LLMs) to generate effective meta information for web content, including article titles, meta titles, meta descriptions, and slugs.

## Core Principles

When prompting an LLM for meta information, always specify these requirements:

1. Every element must be unique across the website
2. Content must accurately reflect the page content
3. No keyword stuffing or hyperbole
4. Mobile-first considerations
5. Action-oriented language with strong verbs

## Article Title (H1) Prompting

Request Format:
```
Please create an article title for a piece about [topic] that:
- Contains the primary keyword: [keyword]
- Is longer than the meta title
- Uses [title case/sentence case] per style guide
- Avoids acronyms
- Clearly indicates the content type (guide, comparison, how-to)
```

Technical Requirements:
- One H1 per page
- Longer than meta title
- Contains primary keyword
- Matches content type

## Meta Title Prompting

Request Format:
```
Generate a meta title for an article about [topic] that:
- Uses different words than the H1 but includes [primary keyword]
- Fits within 50-60 characters for mobile display
- Prioritizes important information in the first 50 characters
- Includes brand name if space permits
```

Technical Requirements:
- 50-70 characters optimal (varies by device)
- Unique across website
- Primary keyword inclusion
- Different wording from H1

## Meta Description Prompting

Request Format:
```
Create a meta description for [content type] about [topic] that:
- Targets [specific search intent: informational/commercial/transactional/navigational]
- Stays within 155-160 characters
- Includes a clear call-to-action
- Matches these search queries: [list relevant queries]
- Uses these keywords naturally: [list keywords]
```

Search Intent Specifications:
- Informational: Focus on knowledge gain, use "Learn," "Discover," "Understand"
- Commercial: Emphasize comparison points, features, benefits
- Transactional: Highlight immediate value, action steps
- Navigational: Confirm resource authenticity, version info

Technical Requirements:
- 155-160 characters optimal
- Unique for each page
- Natural keyword inclusion
- Clear call-to-action
- Match search intent

## Slug Generation Prompting

Request Format:
```
Generate a URL slug from this title: [title] that:
- Uses hyphens between words
- Removes unnecessary words (articles, prepositions)
- Maintains keyword relevance
- Balances length and readability
```

Technical Requirements:
- Hyphen separation
- Keyword inclusion
- Similar to article title
- No special characters
- All lowercase

## Example Prompt Templates

### For Complete Meta Package:
```
Please generate all meta information for an article about [topic]:

Context:
- Primary keyword: [keyword]
- Search intent: [intent type]
- Target audience: [audience]
- Content type: [type]
- Brand name: [brand]
- Style guide preference: [style]

Please provide:
1. Article title (H1)
2. Meta title (50-60 characters)
3. Meta description (155-160 characters)
4. URL slug
```

### For Meta Description Focus:
```
Create a meta description for a [content type] targeting [search intent]:

Parameters:
- Primary keyword: [keyword]
- Target length: 155-160 characters
- Audience level: [beginner/intermediate/expert]
- Key benefit to highlight: [benefit]
- Call-to-action: [desired action]
- Search queries to match: [queries]
```

## Validation Instructions

Always request the LLM to:
1. Check character counts
2. Verify keyword inclusion
3. Confirm uniqueness
4. Test readability
5. Match search intent
6. Provide rationale for choices

## Common Pitfalls to Avoid

Instruct the LLM to avoid:
- Duplicate meta information
- Keyword stuffing
- Misleading descriptions
- Generic calls-to-action
- Overly technical language for general audiences
- Mixing search intents
- Truncated display issues

## Quality Checklist

Final output should:
- Meet character limits
- Include primary keywords naturally
- Match search intent
- Provide clear value proposition
- Use action-oriented language
- Be mobile-friendly
- Maintain brand voice
- Drive click-through with compelling copy

Use this guide to structure your prompts for consistent, effective meta information generation that serves both SEO requirements and user needs.
# Assignment from The Upright Project for Bruce
Date: 2025-01-30 15:00

## 1. Objective

- Companies are represented by their revenue mix, i.e. the share of revenue generated
from each product or service the business markets

    - Example: 80% of Mike’s Fruit Farm’s revenue comes from Apples and 20% from
Pears

- Products and services are modeled as a hierarchy, where all but one root product have
zero to n children
    - Example: Apples and Pears are Fruits. Fruits are Food. Some other things might
be also Food

- The alignment of a given product or service is potentially denoted by one of the
following 4 categories: “strongly aligned”, “aligned”, “misaligned” or “strongly
misaligned”. A product is not necessarily categorized into any of these categories.

- SDG Alignment should be propagated in the taxonomy: if a product has no alignment
defined, it should be considered to be aligned according to the nearest ancestor (dire
parent, parent of parent etc)
    - Example: if Fruits are defined to be aligned towards ending world hunger,
should consider Apples and Pears also aligned, unless otherwise specifi

- There is no set example data, so you should generate some illustrative test examples

- The idea is to create a proof-of-concept that can be demoed and discussed, as well as
reviewed independently. Choice of tech stack is free and you can be creative with the
solution. That said, our software engineers mainly use a stack of PostgreSQL, Node,
React and TypeScript, so showcasing familiarity with any of them is a plus. Most
candidates produce git repositories or zip archives of code and some simple README
to explain how to use the solution

- Further bonus points are awarded for consideration of scalability: our current product
graph contains ~20k products and services (of which ~10k are “leaf products” with no
children), and ~500k companies
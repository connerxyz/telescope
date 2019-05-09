# Navigation processor

Features:

- Generates a navigation section for each notebook
- The navigation section is essentially a Table-of-Contents for each notebook's
content, with each topic linked to its section.
- The navigation processor also adds back-to-top links. These links are handy
for traversing back up to the navigation section.


Navigation-section uses fragment identifier links:

- https://tools.ietf.org/html/rfc2396#section-4.1
- https://www.w3.org/blog/2011/05/hash-uris/

Options

- heading_depth (int): What is the smallest heading that should be linked in 
navigation section? e.g. `4` would mean that `h1-h4` tags would be linked, but 
not `h5` tags.

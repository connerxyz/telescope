# `core`

All the primitives necessary for implementing a notebook service processing pipeline.

### INTERFACES DEFINE THE METHODS WE EXPECT TO BE ABLE TO CALL ON CORE OBJECTS

### CORE OBJECTS PROVIDE DEFAULT IMPLEMENTATIONS

## interfaces

- Interfaces specify which methods are necessary for the architecture patterns employed by the framework to work.
- Interfaces may also provide default implementations.

## core objects

### `Pipeline`

- Inherits from `PipelineInterface`
- Provides a default implementation of `PipelineInteface`

### `Notebook`

- A "business object" for facilitating processing and aggregating with Jupyter notebooks.
- All pipelines, processors, and aggregators operate on `Notebook` instances.

---

## `interfaces`

- Interfaces specify which methods are necessary
- They may also provide default implementations.

This module contains abstract classes used to declare abstract interfaces. 
This is about designing effective `core` primitives: demarcating abstraction layers, 
and specifying how those layers interact (not about providing implementations).

This allows users to define classes that provide higher-order functionality in a way
that  

Here's what happens when you don't satisfy `core.interfaces` declarations: 

```$xslt
# Example of attempting to instantiate a class that does not provide all the necessary implementation
# ...
```

## `mixins`

This module provides implementations of the abstract interfaces declared in `core.interfaces`. That is, each mixin
tightly corresponds with one of the `core.interfaces`, providing implementation of the method(s) it's corresponding 
interface declares.

## Examples

Creating a subclass *only* using an interface and a corresponding mixin.

```$xslt
# TODO
# Example of creating a class that *does* something via mixin inheritance
class GlobNotebookLoader(...
```

Combining interfaces and mixins to compose classes that perform higher-order functions

```$xslt
# TODO
```

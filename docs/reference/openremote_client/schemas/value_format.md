Module openremote_client.schemas.value_format
=============================================

Classes
-------

`ValueFormat(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `asBoolean: bool | None`
    :   The type of the None singleton.

    `asDate: bool | None`
    :   The type of the None singleton.

    `asMomentary: bool | None`
    :   The type of the None singleton.

    `asNumber: bool | None`
    :   The type of the None singleton.

    `asOnOff: bool | None`
    :   The type of the None singleton.

    `asOpenClosed: bool | None`
    :   The type of the None singleton.

    `asPressedReleased: bool | None`
    :   The type of the None singleton.

    `asSlider: bool | None`
    :   The type of the None singleton.

    `dateStyle: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `day: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `dayPeriod: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `era: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `fractionalSecondDigits: int | None`
    :   The type of the None singleton.

    `hour: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `hour12: bool | None`
    :   The type of the None singleton.

    `iso8601: bool | None`
    :   The type of the None singleton.

    `maximumFractionDigits: int | None`
    :   The type of the None singleton.

    `maximumSignificantDigits: int | None`
    :   The type of the None singleton.

    `minimumFractionDigits: int | None`
    :   The type of the None singleton.

    `minimumIntegerDigits: int | None`
    :   The type of the None singleton.

    `minimumSignificantDigits: int | None`
    :   The type of the None singleton.

    `minute: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `momentJsFormat: str | None`
    :   The type of the None singleton.

    `month: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `multiline: bool | None`
    :   The type of the None singleton.

    `resolution: int | None`
    :   The type of the None singleton.

    `second: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `timeStyle: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `timeZoneName: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `useGrouping: bool | None`
    :   The type of the None singleton.

    `week: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `weekday: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.

    `year: Literal['numeric', '2-digit', 'full', 'long', 'medium', 'short', 'narrow'] | None`
    :   The type of the None singleton.
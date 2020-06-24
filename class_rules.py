from exceptions import ClassNameError, ClassAttributeError, NoDocStringError
                        


class Rules(type):

    """ This class is use to impose rules to the classes 
    which implements this class"""

    def __init__(cls, name, bases, attrs):
        super(Rules, cls).__init__(name, bases, attrs)
        
    def __new__(cls, name, bases, attrs):
        cls = type.__new__(cls, name, bases, attrs)
      
        # Verify class name should start with Capital letter else throw error
        if name[0].islower():
            raise ClassNameError("Class name should start with upper case: {name}".format(name=name))

        # Verify whether the class contains `docstring` else raise exception
        # should present, else raise exception
        if not cls.__doc__:
            raise NoDocStringError(
                        f"docstring not present for the class : {name}"
                    )

        # Veryfy class attributes
        # Raise error if not starting with `_` or if it starts with upper case
        malformed_class_attributes = []
        for cls_attr in attrs.keys():
            if (not cls_attr.startswith("_")) and (cls_attr[0].isupper()):
                malformed_class_attributes.append(cls_attr)
        if malformed_class_attributes:
            raise ClassAttributeError(
                f"""Class attributes should start with _ 
                and should not start with Capital letter :
                {malformed_class_attributes}"""
            )
            
        # Verify whether the method contains `docstring` else raise exception
        for attribute in attrs.items():
            if (hasattr(attribute[1], '__call__')) and (not attribute[0].startswith('_')):
                if not attribute[1].__doc__:
                    raise NoDocStringError(
                        f"docstring not present for the method : {attribute[1].__name__}"
                    )
        return cls

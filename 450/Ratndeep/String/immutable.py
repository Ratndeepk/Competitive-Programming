"""
In the String constant pool, 
a String object is likely to have one or many references. 
If several references point to same String without even knowing it, 
it would be bad if one of the references modified that String value. 
That's why String objects are immutable.
"""
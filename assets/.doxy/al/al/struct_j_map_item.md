

# Struct JMapItem



[**ClassList**](annotated.md) **>** [**JMapItem**](struct_j_map_item.md)





* `#include <alJMapInfo.h>`

















## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**Type**](#enum-type)  <br> |




## Public Attributes

| Type | Name |
| ---: | :--- |
|  u16 | [**mDataOffset**](#variable-mdataoffset)  <br> |
|  u32 | [**mHash**](#variable-mhash)  <br> |
|  u32 | [**mMask**](#variable-mmask)  <br> |
|  u8 | [**mShift**](#variable-mshift)  <br> |
|  [**Type**](struct_j_map_item.md#enum-type) | [**mType**](#variable-mtype)  <br> |












































## Public Types Documentation




### enum Type 

```C++
enum JMapItem::Type {
    Long,
    String,
    Float,
    Long2,
    Short,
    Byte,
    StringPtr,
    Null
};
```




<hr>
## Public Attributes Documentation




### variable mDataOffset 

```C++
u16 JMapItem::mDataOffset;
```




<hr>



### variable mHash 

```C++
u32 JMapItem::mHash;
```




<hr>



### variable mMask 

```C++
u32 JMapItem::mMask;
```




<hr>



### variable mShift 

```C++
u8 JMapItem::mShift;
```




<hr>



### variable mType 

```C++
Type JMapItem::mType;
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/Util/alJMapInfo.h`


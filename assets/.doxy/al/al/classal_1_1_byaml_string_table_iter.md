

# Class al::ByamlStringTableIter



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**ByamlStringTableIter**](classal_1_1_byaml_string_table_iter.md)





* `#include <alByamlStringTableIter.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \* | [**mData**](#variable-mdata)  <br> |
|  [**uintptr\_t**](classal_1_1_functor_v0_m.md) | [**mDataPtr**](#variable-mdataptr)  <br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**Header**](structal_1_1_byaml_string_table_iter_1_1_header.md) \* | [**mHeader**](#variable-mheader)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ByamlStringTableIter**](#function-byamlstringtableiter) ([**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \* data) <br> |
|  [**int**](classal_1_1_functor_v0_m.md) | [**findStringIndex**](#function-findstringindex) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* str) const<br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**u32**](classal_1_1_functor_v0_m.md) \* | [**getAddressTable**](#function-getaddresstable) () const<br> |




























## Public Attributes Documentation




### variable mData 

```C++
const u8* al::ByamlStringTableIter::mData;
```




<hr>



### variable mDataPtr 

```C++
uintptr_t al::ByamlStringTableIter::mDataPtr;
```




<hr>



### variable mHeader 

```C++
const Header* al::ByamlStringTableIter::mHeader;
```




<hr>
## Public Functions Documentation




### function ByamlStringTableIter 

```C++
inline al::ByamlStringTableIter::ByamlStringTableIter (
    const  u8 * data
) 
```




<hr>



### function findStringIndex 

```C++
int al::ByamlStringTableIter::findStringIndex (
    const  char * str
) const
```




<hr>



### function getAddressTable 

```C++
inline const  u32 * al::ByamlStringTableIter::getAddressTable () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/Yaml/alByamlStringTableIter.h`


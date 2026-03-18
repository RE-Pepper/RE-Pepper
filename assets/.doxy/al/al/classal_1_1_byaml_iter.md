

# Class al::ByamlIter



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**ByamlIter**](classal_1_1_byaml_iter.md)





* `#include <alByamlIter.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**const**](classal_1_1_functor_v0_m.md) [**ByamlContainerHeader**](classal_1_1_byaml_container_header.md) \* | [**mContainerHeader**](#variable-mcontainerheader)  <br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \* | [**mData**](#variable-mdata)  <br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**ByamlHeader**](classal_1_1_byaml_header.md) \* | [**mHeader**](#variable-mheader)  <br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \* | [**mRootNode**](#variable-mrootnode)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ByamlIter**](#function-byamliter-14) () <br> |
|   | [**ByamlIter**](#function-byamliter-24) ([**const**](classal_1_1_functor_v0_m.md) [**ByamlIter**](classal_1_1_byaml_iter.md) & other) <br> |
|   | [**ByamlIter**](#function-byamliter-34) ([**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \* data) <br> |
|   | [**ByamlIter**](#function-byamliter-44) ([**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \* data, [**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \* rootNode) <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**getByamlDataAndKeyName**](#function-getbyamldataandkeyname) ([**ByamlData**](classal_1_1_byaml_data.md) \* out, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \*\* key, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**getByamlDataByIndex**](#function-getbyamldatabyindex) ([**ByamlData**](classal_1_1_byaml_data.md) \* out, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**getByamlDataByKey**](#function-getbyamldatabykey) ([**ByamlData**](classal_1_1_byaml_data.md) \* out, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* key) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**getByamlDataByKeyIndex**](#function-getbyamldatabykeyindex) ([**ByamlData**](classal_1_1_byaml_data.md) \* out, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**ByamlHeader**](classal_1_1_byaml_header.md) \* | [**getHeader**](#function-getheader) () const<br> |
|  [**ByamlIter**](classal_1_1_byaml_iter.md) | [**getIterByIndex**](#function-getiterbyindex) ([**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**ByamlIter**](classal_1_1_byaml_iter.md) | [**getIterByKey**](#function-getiterbykey) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* key) const<br> |
|  [**int**](classal_1_1_functor_v0_m.md) | [**getKeyIndex**](#function-getkeyindex) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* key) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**getKeyName**](#function-getkeyname) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \*\* out, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**int**](classal_1_1_functor_v0_m.md) | [**getSize**](#function-getsize) () const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isEqualData**](#function-isequaldata) ([**const**](classal_1_1_functor_v0_m.md) [**ByamlIter**](classal_1_1_byaml_iter.md) & other) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isExistKey**](#function-isexistkey) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* key) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isTypeArray**](#function-istypearray) () const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isTypeContainer**](#function-istypecontainer) () const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isTypeHash**](#function-istypehash) () const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isValid**](#function-isvalid) () const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryConvertBinary**](#function-tryconvertbinary) ([**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \*\* out, [**int**](classal_1_1_functor_v0_m.md) \* size, [**const**](classal_1_1_functor_v0_m.md) [**ByamlData**](classal_1_1_byaml_data.md) \* data) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryConvertBool**](#function-tryconvertbool) ([**bool**](classal_1_1_functor_v0_m.md) \* out, [**const**](classal_1_1_functor_v0_m.md) [**ByamlData**](classal_1_1_byaml_data.md) \* data) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryConvertFloat**](#function-tryconvertfloat) ([**float**](classal_1_1_functor_v0_m.md) \* out, [**const**](classal_1_1_functor_v0_m.md) [**ByamlData**](classal_1_1_byaml_data.md) \* data) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryConvertInt**](#function-tryconvertint) ([**int**](classal_1_1_functor_v0_m.md) \* out, [**const**](classal_1_1_functor_v0_m.md) [**ByamlData**](classal_1_1_byaml_data.md) \* data) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryConvertIter**](#function-tryconvertiter) ([**ByamlIter**](classal_1_1_byaml_iter.md) \* iter, [**const**](classal_1_1_functor_v0_m.md) [**ByamlData**](classal_1_1_byaml_data.md) \* data) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryConvertString**](#function-tryconvertstring) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \*\* out, [**const**](classal_1_1_functor_v0_m.md) [**ByamlData**](classal_1_1_byaml_data.md) \* data) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetBinaryByIndex**](#function-trygetbinarybyindex) ([**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \*\* out, [**int**](classal_1_1_functor_v0_m.md) \* size, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetBinaryByKey**](#function-trygetbinarybykey) ([**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \*\* out, [**int**](classal_1_1_functor_v0_m.md) \* size, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* key) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetBoolByIndex**](#function-trygetboolbyindex) ([**bool**](classal_1_1_functor_v0_m.md) \* out, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetBoolByKey**](#function-trygetboolbykey) ([**bool**](classal_1_1_functor_v0_m.md) \* out, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* key) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetFloatByIndex**](#function-trygetfloatbyindex) ([**float**](classal_1_1_functor_v0_m.md) \* out, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetFloatByKey**](#function-trygetfloatbykey) ([**float**](classal_1_1_functor_v0_m.md) \* out, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* key) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetIntByIndex**](#function-trygetintbyindex) ([**int**](classal_1_1_functor_v0_m.md) \* out, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetIntByKey**](#function-trygetintbykey) ([**int**](classal_1_1_functor_v0_m.md) \* out, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* key) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetIterAndKeyNameByIndex**](#function-trygetiterandkeynamebyindex) ([**ByamlIter**](classal_1_1_byaml_iter.md) \* out, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \*\* key, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetIterByIndex**](#function-trygetiterbyindex) ([**ByamlIter**](classal_1_1_byaml_iter.md) \* out, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetIterByKey**](#function-trygetiterbykey) ([**ByamlIter**](classal_1_1_byaml_iter.md) \* out, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* key) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetStringByIndex**](#function-trygetstringbyindex) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \*\* out, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**tryGetStringByKey**](#function-trygetstringbykey) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \*\* out, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* key) const<br> |




























## Public Attributes Documentation




### variable mContainerHeader 

```C++
const ByamlContainerHeader* al::ByamlIter::mContainerHeader;
```




<hr>



### variable mData 

```C++
const u8* al::ByamlIter::mData;
```




<hr>



### variable mHeader 

```C++
const ByamlHeader* al::ByamlIter::mHeader;
```




<hr>



### variable mRootNode 

```C++
const u8* al::ByamlIter::mRootNode;
```




<hr>
## Public Functions Documentation




### function ByamlIter [1/4]

```C++
al::ByamlIter::ByamlIter () 
```




<hr>



### function ByamlIter [2/4]

```C++
al::ByamlIter::ByamlIter (
    const  ByamlIter & other
) 
```




<hr>



### function ByamlIter [3/4]

```C++
al::ByamlIter::ByamlIter (
    const  u8 * data
) 
```




<hr>



### function ByamlIter [4/4]

```C++
al::ByamlIter::ByamlIter (
    const  u8 * data,
    const  u8 * rootNode
) 
```




<hr>



### function getByamlDataAndKeyName 

```C++
bool al::ByamlIter::getByamlDataAndKeyName (
    ByamlData * out,
    const  char ** key,
    int index
) const
```




<hr>



### function getByamlDataByIndex 

```C++
bool al::ByamlIter::getByamlDataByIndex (
    ByamlData * out,
    int index
) const
```




<hr>



### function getByamlDataByKey 

```C++
bool al::ByamlIter::getByamlDataByKey (
    ByamlData * out,
    const  char * key
) const
```




<hr>



### function getByamlDataByKeyIndex 

```C++
bool al::ByamlIter::getByamlDataByKeyIndex (
    ByamlData * out,
    int index
) const
```




<hr>



### function getHeader 

```C++
inline const  ByamlHeader * al::ByamlIter::getHeader () const
```




<hr>



### function getIterByIndex 

```C++
ByamlIter al::ByamlIter::getIterByIndex (
    int index
) const
```




<hr>



### function getIterByKey 

```C++
ByamlIter al::ByamlIter::getIterByKey (
    const  char * key
) const
```




<hr>



### function getKeyIndex 

```C++
int al::ByamlIter::getKeyIndex (
    const  char * key
) const
```




<hr>



### function getKeyName 

```C++
bool al::ByamlIter::getKeyName (
    const  char ** out,
    int index
) const
```




<hr>



### function getSize 

```C++
int al::ByamlIter::getSize () const
```




<hr>



### function isEqualData 

```C++
bool al::ByamlIter::isEqualData (
    const  ByamlIter & other
) const
```




<hr>



### function isExistKey 

```C++
bool al::ByamlIter::isExistKey (
    const  char * key
) const
```




<hr>



### function isTypeArray 

```C++
bool al::ByamlIter::isTypeArray () const
```




<hr>



### function isTypeContainer 

```C++
bool al::ByamlIter::isTypeContainer () const
```




<hr>



### function isTypeHash 

```C++
bool al::ByamlIter::isTypeHash () const
```




<hr>



### function isValid 

```C++
bool al::ByamlIter::isValid () const
```




<hr>



### function tryConvertBinary 

```C++
bool al::ByamlIter::tryConvertBinary (
    const  u8 ** out,
    int * size,
    const  ByamlData * data
) const
```




<hr>



### function tryConvertBool 

```C++
bool al::ByamlIter::tryConvertBool (
    bool * out,
    const  ByamlData * data
) const
```




<hr>



### function tryConvertFloat 

```C++
bool al::ByamlIter::tryConvertFloat (
    float * out,
    const  ByamlData * data
) const
```




<hr>



### function tryConvertInt 

```C++
bool al::ByamlIter::tryConvertInt (
    int * out,
    const  ByamlData * data
) const
```




<hr>



### function tryConvertIter 

```C++
bool al::ByamlIter::tryConvertIter (
    ByamlIter * iter,
    const  ByamlData * data
) const
```




<hr>



### function tryConvertString 

```C++
bool al::ByamlIter::tryConvertString (
    const  char ** out,
    const  ByamlData * data
) const
```




<hr>



### function tryGetBinaryByIndex 

```C++
bool al::ByamlIter::tryGetBinaryByIndex (
    const  u8 ** out,
    int * size,
    int index
) const
```




<hr>



### function tryGetBinaryByKey 

```C++
bool al::ByamlIter::tryGetBinaryByKey (
    const  u8 ** out,
    int * size,
    const  char * key
) const
```




<hr>



### function tryGetBoolByIndex 

```C++
bool al::ByamlIter::tryGetBoolByIndex (
    bool * out,
    int index
) const
```




<hr>



### function tryGetBoolByKey 

```C++
bool al::ByamlIter::tryGetBoolByKey (
    bool * out,
    const  char * key
) const
```




<hr>



### function tryGetFloatByIndex 

```C++
bool al::ByamlIter::tryGetFloatByIndex (
    float * out,
    int index
) const
```




<hr>



### function tryGetFloatByKey 

```C++
bool al::ByamlIter::tryGetFloatByKey (
    float * out,
    const  char * key
) const
```




<hr>



### function tryGetIntByIndex 

```C++
bool al::ByamlIter::tryGetIntByIndex (
    int * out,
    int index
) const
```




<hr>



### function tryGetIntByKey 

```C++
bool al::ByamlIter::tryGetIntByKey (
    int * out,
    const  char * key
) const
```




<hr>



### function tryGetIterAndKeyNameByIndex 

```C++
bool al::ByamlIter::tryGetIterAndKeyNameByIndex (
    ByamlIter * out,
    const  char ** key,
    int index
) const
```




<hr>



### function tryGetIterByIndex 

```C++
bool al::ByamlIter::tryGetIterByIndex (
    ByamlIter * out,
    int index
) const
```




<hr>



### function tryGetIterByKey 

```C++
bool al::ByamlIter::tryGetIterByKey (
    ByamlIter * out,
    const  char * key
) const
```




<hr>



### function tryGetStringByIndex 

```C++
bool al::ByamlIter::tryGetStringByIndex (
    const  char ** out,
    int index
) const
```




<hr>



### function tryGetStringByKey 

```C++
bool al::ByamlIter::tryGetStringByKey (
    const  char ** out,
    const  char * key
) const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/Yaml/alByamlIter.h`


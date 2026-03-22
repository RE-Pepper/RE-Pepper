

# Class al::ByamlHashIter



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**ByamlHashIter**](classal_1_1_byaml_hash_iter.md)





* `#include <alByamlHashIter.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \* | [**mData**](#variable-mdata)  <br> |
|  [**uintptr\_t**](classal_1_1_functor_v0_m.md) | [**mDataPtr**](#variable-mdataptr)  <br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**Header**](structal_1_1_byaml_hash_iter_1_1_header.md) \* | [**mHeader**](#variable-mheader)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ByamlHashIter**](#function-byamlhashiter) ([**const**](classal_1_1_functor_v0_m.md) [**u8**](classal_1_1_functor_v0_m.md) \* data) <br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**ByamlHashPair**](classal_1_1_byaml_hash_pair.md) \* | [**findPair**](#function-findpair) ([**int**](classal_1_1_functor_v0_m.md) keyIdx) const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**getDataByKey**](#function-getdatabykey) ([**ByamlData**](classal_1_1_byaml_data.md) \* out, [**int**](classal_1_1_functor_v0_m.md) index) const<br> |




























## Public Attributes Documentation




### variable mData 

```C++
const u8* al::ByamlHashIter::mData;
```




<hr>



### variable mDataPtr 

```C++
uintptr_t al::ByamlHashIter::mDataPtr;
```




<hr>



### variable mHeader 

```C++
const Header* al::ByamlHashIter::mHeader;
```




<hr>
## Public Functions Documentation




### function ByamlHashIter 

```C++
inline al::ByamlHashIter::ByamlHashIter (
    const  u8 * data
) 
```




<hr>



### function findPair 

```C++
const  ByamlHashPair * al::ByamlHashIter::findPair (
    int keyIdx
) const
```




<hr>



### function getDataByKey 

```C++
bool al::ByamlHashIter::getDataByKey (
    ByamlData * out,
    int index
) const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/Yaml/alByamlHashIter.h`


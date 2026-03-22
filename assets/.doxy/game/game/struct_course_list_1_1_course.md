

# Struct CourseList::Course



[**ClassList**](annotated.md) **>** [**Course**](struct_course_list_1_1_course.md)






















## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**CourseType**](#enum-coursetype)  <br> |




## Public Attributes

| Type | Name |
| ---: | :--- |
|  int | [**mCoinCollectNum**](#variable-mcoincollectnum)  <br> |
|  int | [**mCourseType**](#variable-mcoursetype)  <br> |
|  const char \* | [**mMiniatureModelName**](#variable-mminiaturemodelname)  <br> |
|  int | [**mScenario**](#variable-mscenario)  <br> |
|  const char \* | [**mStageName**](#variable-mstagename)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Course**](#function-course) (const al::ByamlIter \* course) <br> |


## Public Static Functions

| Type | Name |
| ---: | :--- |
|  bool | [**isCourseTypeStage**](#function-iscoursetypestage) ([**CourseType**](struct_course_list_1_1_course.md#enum-coursetype) type) <br> |


























## Public Types Documentation




### enum CourseType 

```C++
enum Course::CourseType {
    CourseType_Normal,
    CourseType_KoopaCastle,
    CourseType_KoopaFortress,
    CourseType_KoopaBattleShip,
    CourseType_Championship,
    CourseType_KinopioHousePresent,
    CourseType_KinopioHouseAlbum,
    CourseType_MysteryBox,
    CourseType_Dokan,
    CourseType_Empty = 10
};
```




<hr>
## Public Attributes Documentation




### variable mCoinCollectNum 

```C++
int CourseList::Course::mCoinCollectNum;
```




<hr>



### variable mCourseType 

```C++
int CourseList::Course::mCourseType;
```




<hr>



### variable mMiniatureModelName 

```C++
const char* CourseList::Course::mMiniatureModelName;
```




<hr>



### variable mScenario 

```C++
int CourseList::Course::mScenario;
```




<hr>



### variable mStageName 

```C++
const char* CourseList::Course::mStageName;
```




<hr>
## Public Functions Documentation




### function Course 

```C++
Course::Course (
    const al::ByamlIter * course
) 
```




<hr>
## Public Static Functions Documentation




### function isCourseTypeStage 

```C++
static bool Course::isCourseTypeStage (
    CourseType type
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/System/CourseList.h`


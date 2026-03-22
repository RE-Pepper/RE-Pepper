

# File CourseList.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**System**](dir_e1006d71d276319c0715d176f1f44d04.md) **>** [**CourseList.h**](_course_list_8h.md)

[Go to the documentation of this file](_course_list_8h.md)


```C++
#pragma once

namespace al
{
class Resource;
class ByamlIter;
} // namespace al

class CourseList
{
public:
        void init( const al::Resource* gameSystemDataTable );

private:
        struct Course
        {
                enum CourseType
                {
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

                int         mCourseType;
                const char* mStageName;
                int         mScenario;
                const char* mMiniatureModelName;
                int         mCoinCollectNum;

                Course( const al::ByamlIter* course );

                static bool isCourseTypeStage( CourseType type );
        };

        struct World
        {
                Course** mCourses;
                int      mNumCourses;
                bool     mIsSpecialWorld;

                World( const al::ByamlIter* world );
        };

        struct List
        {
                World** mWorlds;
                int     mNumWorlds;

                List( const al::ByamlIter& courseListIter );
        };

        List* mCourseList;
        int   mNumStages;

public:
        CourseList();
};

namespace rp
{

CourseList* getCourseList();

} // namespace rp
```



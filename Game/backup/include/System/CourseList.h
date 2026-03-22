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

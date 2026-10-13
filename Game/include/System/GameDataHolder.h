#pragma once

namespace al
{
class LayoutInitInfo;
}
class CourseList;
class GameDataFile;
class SaveDataFile;
class SaveDataAccessSequence

        class GameDataHolder
{
private:
        GameDataFile*           mGameFile;
        SaveDataFile*           mSaveFiles;
        int                     mCurSaveFileIdx;
        SaveDataAccessSequence* mSaveAccess;

public:
        void createSaveDataAccessSequence( const al::LayoutInitInfo& info );

public:
        GameDataHolder( CourseList* courseList );
};

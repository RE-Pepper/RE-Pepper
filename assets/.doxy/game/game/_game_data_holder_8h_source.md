

# File GameDataHolder.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**System**](dir_e1006d71d276319c0715d176f1f44d04.md) **>** [**GameDataHolder.h**](_game_data_holder_8h.md)

[Go to the documentation of this file](_game_data_holder_8h.md)


```C++
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
```



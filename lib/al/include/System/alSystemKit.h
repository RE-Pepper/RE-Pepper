#pragma once

#include <heap/seadHeap.h>

namespace al
{
class MemorySystem;
class FileLoader;
class SaveDataDirector;

class SystemKit
{
private:
        MemorySystem*     mMemorySystem;
        FileLoader*       mFileLoader;
        void*             _8;
        SaveDataDirector* mSaveDataDirector;
        void*             _10[ 7 ];

public:
        MemorySystem* getMemorySystem() const
        {
                return mMemorySystem;
        }

        FileLoader* getFileLoader() const
        {
                return mFileLoader;
        }

        SaveDataDirector* getSaveDataDirector() const
        {
                return mSaveDataDirector;
        }

        void createFileLoader( int r1 );
        void createSaveDataSystem( u32 r1, s32 r2 );
};

} // namespace al

namespace alProjectInterface
{

al::SystemKit* getSystemKit();

} // namespace alProjectInterface

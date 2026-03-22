

# File alSystemKit.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**System**](dir_61ffa07cfbda06360481d678005eeea2.md) **>** [**alSystemKit.h**](al_system_kit_8h.md)

[Go to the documentation of this file](al_system_kit_8h.md)


```C++
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
```



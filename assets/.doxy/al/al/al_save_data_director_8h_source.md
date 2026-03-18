

# File alSaveDataDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Save**](dir_fec35835b019f224ced7f4d2afb3cf47.md) **>** [**alSaveDataDirector.h**](al_save_data_director_8h.md)

[Go to the documentation of this file](al_save_data_director_8h.md)


```C++
#pragma once

namespace al
{
class SaveDataSequenceBase;
class SaveDataSequenceInitDir;
class AsyncFunctorThread;

class SaveDataDirector
{
private:
        void*                     _0;
        SaveDataSequenceBase*     _4;
        SaveDataSequenceBase*     _8;
        SaveDataSequenceInitDir*  mInitDirSequence;
        u8                        _10[ 0x58 ];
        class AsyncFunctorThread* mSaveDataThread;
        void*                     _6C;

public:
        SaveDataDirector( u32, s32 );
};

} // namespace al
```



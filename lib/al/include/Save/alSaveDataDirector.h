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



# File alSequence.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Sequence**](dir_82a3f069d834280ed17bc3feb81358ab.md) **>** [**alSequence.h**](al_sequence_8h.md)

[Go to the documentation of this file](al_sequence_8h.md)


```C++
#pragma once

#include <Nerve/alNerveExecutor.h>
#include <prim/seadSafeString.h>

namespace al
{
class Scene;

class Sequence : public NerveExecutor
{
private:
        sead::FixedSafeString<64> mName;
        Scene*                    mCurrentScene;
        u8                        unk[ 0xf0 ];

public:
        virtual void init( /*SequenceInitInfo& ?*/ );
        virtual void update();
        virtual void unk1();
        virtual void unk2();
        virtual void unk3();
        virtual bool isDisposable() const;
        virtual bool unk4();
        virtual int  unk5();
        virtual int  unk6();

public:
        Sequence( const char* name );
};

} // namespace al
```



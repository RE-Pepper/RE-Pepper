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

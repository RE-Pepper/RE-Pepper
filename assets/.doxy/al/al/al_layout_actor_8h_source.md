

# File alLayoutActor.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Layout**](dir_df428175ad75013516ece83f85ae05d3.md) **>** [**alLayoutActor.h**](al_layout_actor_8h.md)

[Go to the documentation of this file](al_layout_actor_8h.md)


```C++
#pragma once

#include <Audio/alAudioKeeper.h>
#include <Effect/alEffectKeeper.h>
#include <Nerve/alNerve.h>
#include <prim/seadSafeString.h>

namespace al
{
class LayoutInitInfo;
class NerveKeeper;

class LayoutActor : public IUseNerve, public IUseAudioKeeper, public IUseEffectKeeper
{
protected:
        sead::SafeString mName;
        NerveKeeper*     mNerveKeeper;
        AudioKeeper*     mAudioKeeper;
        EffectKeeper*    mEffectKeeper;
        void*            _20;
        void*            _24;
        void*            _28;
        bool             mIsAlive;

public:
        void initNerve( const Nerve* nerve, int maxNerveStates = 0 );

public:
        virtual NerveKeeper*  getNerveKeeper() const;
        virtual void          appear();
        virtual void          kill();
        virtual void          movement();
        virtual void          calcAnim();
        virtual AudioKeeper*  getAudioKeeper() const;
        virtual EffectKeeper* getEffectKeeper() const;
        virtual void          control();
        virtual void          unk1();
        virtual void          unk2();

public:
        LayoutActor( const char* name );
};

void initLayoutActor( LayoutActor* layoutActor, const LayoutInitInfo& info, const char* archiveName, const char* = nullptr );

void  startAction( LayoutActor* actor, const sead::SafeString& actionName );
bool  isActionEnd( const LayoutActor* actor );
void  setActionFrameRate( LayoutActor* actor, float rate );
float getActionFrameMax( const LayoutActor* actor );

void setPaneString( LayoutActor* actor, const char* paneName, const wchar_t* text );
void hidePane( LayoutActor* actor, const char* paneName );

} // namespace al
```



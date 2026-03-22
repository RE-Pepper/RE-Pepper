

# File alBreakModel.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Npc**](dir_be9125abb251b9d49bf58065264ab1d9.md) **>** [**alBreakModel.cpp**](al_break_model_8cpp.md)

[Go to the documentation of this file](al_break_model_8cpp.md)


```C++
#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alActorPoseKeeper.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>
#include <Npc/alBreakModel.h>

namespace al
{

namespace NrvBreakModel
{

NERVE_DEF( BreakModel, Wait )
NERVE_DEF( BreakModel, Break )

} // namespace NrvBreakModel

BreakModel::BreakModel( LiveActor* parent, const char* name, const char* modelArchiveName, const sead::Matrix34f* parentBaseMtx, const char* breakActionName )
    : LiveActor( name ), mParent( parent ), mParentBaseMtx( parentBaseMtx ),
      mModelArchiveName( modelArchiveName ), mBreakActionName( breakActionName )
{
}

void BreakModel::init( const ActorInitInfo& info )
{
        initActorWithArchiveName( this, info, mModelArchiveName );
        initNerve( this, &NrvBreakModel::Wait );
        invalidateClipping( this );
        makeActorDead();
}

void BreakModel::appear()
{
        if ( mParentBaseMtx )
                updatePoseMtx( this, mParentBaseMtx );
        else
                copyPose( this, mParent );

        if ( mBreakActionName )
                startAction( this, mBreakActionName );

        setNerve( this, &NrvBreakModel::Break );
        LiveActor::makeActorAppeared();
}

void BreakModel::exeWait()
{
}

void BreakModel::exeBreak()
{
        if ( isActionEnd( this ) )
                kill();
}

} // namespace al
```



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

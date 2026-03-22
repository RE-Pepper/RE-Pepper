#include "Player/GhostPlayer.h"

#include <LiveActor/alActorActionKeeper.h>
#include <LiveActor/alHitSensorFunction.h>
#include <LiveActor/alSensorMsg.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>

#include "Player/GhostPlayerRecorder.h"
#include "Scene/SceneObjFactory.h"
#include "Util/SensorMsg.h"

namespace NrvGhostPlayer
{

NERVE_DEF( GhostPlayer, Begin );
NERVE_DEF( GhostPlayer, Nrv5 );

} // namespace NrvGhostPlayer

GhostPlayer::GhostPlayer( const sead::SafeString& name )
    : MapObjActor( name ), _64( false ), _65( false ), _66( false ), _67( false ), _68( false ), _69( true ),
      _6A( false ), _6B( true ), _6C( false ), _70( -1 ), _74( -1 ), _78( -1 )
{
        GhostPlayerRecorder* recorder =
                static_cast<GhostPlayerRecorder*>( al::createSceneObj( SceneObjType_GhostPlayerRecorder ) );
        if ( recorder->mFrames == nullptr )
                recorder->create( 30 );
        recorder->initGhostPlayer( this );
}

#ifdef NON_MATCHING
void GhostPlayer::init( const al::ActorInitInfo& info )
{
}

void GhostPlayer::kill()
{
        al::startHitReactionDeath( this );
        LiveActor::kill();
}
#endif

void GhostPlayer::attackSensor( al::HitSensor* me, al::HitSensor* other )
{
        if ( !_64 && al::isNerve( this, &NrvGhostPlayer::Begin ) )
        {
                if ( al::isSensorPlayer( other ) )
                {
                        if ( _6A && !al::isSensorEnemyAttack( me ) )
                                return;
                        al::sendMsgEnemyAttack( other, me );
                }
                if ( _6A && al::isSensorMapObj( other ) )
                        al::sendMsg53( other, me );
        }
}

bool GhostPlayer::receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me )
{
        if ( al::isMsgPlayerInvincibleAttack( msg ) && al::isNerve( this, &NrvGhostPlayer::Begin ) )
        {
                rp::requestHitReactionToAttacker( msg, me, other );
                al::startHitReactionDeath( this );
                al::setNerve( this, &NrvGhostPlayer::Nrv5 );
                return true;
        }
        return false;
}

#ifdef NON_MATCHING
void GhostPlayer::control()
{
}
#endif

#ifdef NON_MATCHING
void GhostPlayer::exeHide()
{
}
#endif

#ifdef NON_MATCHING
void GhostPlayer::exeBegin()
{
}
#endif

#ifdef NON_MATCHING
void GhostPlayer::exeNrv5()
{
}
#endif

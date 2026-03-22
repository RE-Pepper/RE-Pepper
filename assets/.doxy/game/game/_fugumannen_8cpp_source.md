

# File Fugumannen.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Enemy**](dir_0e41e8db2a159a2532eb8129063edf58.md) **>** [**Fugumannen.cpp**](_fugumannen_8cpp.md)

[Go to the documentation of this file](_fugumannen_8cpp.md)


```C++
#include "Enemy/Fugumannen.h"

#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alHitSensorFunction.h>
#include <LiveActor/alLiveActorFunction.h>
#include <LiveActor/alSensorMsg.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>
#include <Placement/alPlacementFunction.h>
#include <Rail/alRailFunction.h>

#include "Enemy/EnemyStateBlowDown.h"

namespace NrvFugumannen
{

NERVE_DEF( Fugumannen, Move )
NERVE_DEF( Fugumannen, Move2 )
NERVE_DEF( Fugumannen, BlowDown )

} // namespace NrvFugumannen

Fugumannen::Fugumannen( const sead::SafeString& name )
    : MapObjActor( name ), mRailMoveSpeed( 10.0 ), mStateBlowDown( nullptr )
{
}

extern "C" void fn_0027b51c( al::LiveActor*, const al::ActorInitInfo& info, int );
extern "C" void fn_0027ee34( al::LiveActor*, const al::ActorInitInfo& info, int );

void Fugumannen::init( const al::ActorInitInfo& info )
{
        al::initActor( this, info );
        al::tryGetArg0( &mRailMoveSpeed, info );
        if ( al::isExistRail( info ) )
        {
                initRailKeeper( info );
                al::setSyncRailToStart( this );
        }
        al::initNerve( this, &NrvFugumannen::Move, 1 );
        mStateBlowDown = new EnemyStateBlowDown( this, nullptr, "SwimBlowDown", 1 );
        al::initNerveState( this, mStateBlowDown, &NrvFugumannen::BlowDown, "state:BlowDown" );
        al::startAction( this, "SwimWait" );
        fn_0027b51c( this, info, 3 );
        fn_0027ee34( this, info, 3 );
        al::offCollide( this );
        makeActorAppeared();
}

void Fugumannen::attackSensor( al::HitSensor* me, al::HitSensor* other )
{
        if ( !al::isNerve( this, &NrvFugumannen::BlowDown ) && al::isSensorName( me, "Attack" ) )
        {
                al::sendMsg41( other, me );
                al::sendMsgEnemyAttack( other, me );
        }
}

extern "C" bool fn_0027b768( u32, al::HitSensor*, al::HitSensor*, al::NerveStateBase*, const al::Nerve* );
extern "C" bool fn_0027b704( u32, al::HitSensor*, al::HitSensor*, al::NerveStateBase* );

bool Fugumannen::receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me )
{
        if ( al::isNerve( this, &NrvFugumannen::BlowDown ) || al::isSensorName( me, "Attack" ) )
                return false;

        bool rv = fn_0027b768( msg, other, me, mStateBlowDown, &NrvFugumannen::BlowDown );
        if ( rv ) // :skull:?
                rv = true;

        if ( !rv && ( rv = al::isMsg9( msg ), rv ) )
        {
                fn_0027b704( msg, other, me, mStateBlowDown );
                al::setNerve( this, &NrvFugumannen::BlowDown );
                return true;
        }

        return rv;
}

extern "C" void fn_00240e08( al::LiveActor*, const sead::Vector3f&, float );

void Fugumannen::exeMove()
{
        al::moveSyncRailTurn( this, mRailMoveSpeed );
        sead::Vector3f railDir = al::getRailDir( this );
        if ( !al::isLoopRail( this ) )
                railDir *= -1;
        fn_00240e08( this, railDir, 4.0 );
        if ( al::isRailReachedGoal( this ) )
                al::setNerve( this, &NrvFugumannen::Move2 );
}

void Fugumannen::exeMove2()
{
        sead::Vector3f railDir = al::getRailDir( this );
        if ( !al::isLoopRail( this ) )
                railDir *= -1;
        fn_00240e08( this, railDir, 4.0 );
        if ( al::isGreaterStep( this, 45 ) )
                al::setNerve( this, &NrvFugumannen::Move );
}

extern "C" void fn_002cd428( al::LiveActor*, al::NerveStateBase* );

void Fugumannen::exeBlowDown()
{
        if ( al::updateNerveState( this ) )
        {
                fn_002cd428( this, mStateBlowDown );
                kill();
        }
}
```





# File Togezo.cpp

[**File List**](files.md) **>** [**Enemy**](dir_ee967774be101b809d25f7ebc425a3fb.md) **>** [**Togezo.cpp**](_togezo_8cpp.md)

[Go to the documentation of this file](_togezo_8cpp.md)


```C++
#include "Enemy/Togezo.h"

#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alActorPoseKeeper.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>
#include <Nerve/alNerveStateBase.h>
#include <math/seadVector.h>

#include "Enemy/EnemyStateBlowDown.h"
#include "Enemy/WalkerStateChase.h"
#include "Enemy/WalkerStateChaseParam.h"
#include "Enemy/WalkerStateParam.h"
#include "Enemy/WalkerStateWander.h"
#include "Enemy/WalkerStateWanderParam.h"
#include "Player/PlayerFunction.h"

namespace NrvTogezo
{

NERVE_DEF( Togezo, Wander );
NERVE_DEF( Togezo, Turn );
NERVE_DEF( Togezo, Search );
NERVE_DEF( Togezo, Chase );
NERVE_DEF( Togezo, Attack );
NERVE_DEF( Togezo, BlowDown );

} // namespace NrvTogezo

static WalkerStateParam       split( sTogezoWalkerStateParam )( 4.0, 0.98, 0.85, 250.0, 700.0, 180.0, 70.0, 150.0 );
static WalkerStateWanderParam split( sTogezoWalkerStateWanderParam )( 30, 90, 0.7, 4.0, 10.0, "Walk", "Wait" );
static WalkerStateChaseParam  split( sTogezoWalkerStateChaseParam )( false, true, 1.3, 30.0, 150.0, 3.0, 20.0, "Run", "Wait" );

Togezo::Togezo( const sead::SafeString& name )
    : MapObjActor( name ), mWanderState( nullptr ), mChaseState( nullptr ), mBlowDownState( nullptr )
{
}

extern "C" void fn_0027a1a0( al::LiveActor* actor, const char* ); // inits al::Collider->_4
extern "C" void fn_0027cf20( al::LiveActor* actor, const al::ActorInitInfo& info, int );

#ifdef NON_MATCHING

// inline nop
void Togezo::init( const al::ActorInitInfo& info )
{
        al::initActorWithArchiveName( this, info, "Togezo" );
        fn_0027a1a0( this, "移動制限" );
        fn_0027cf20( this, info, 1 );
        al::initNerve( this, &NrvTogezo::Wander, 3 );
        mWanderState   = new WalkerStateWander( this, al::getFrontPtr( this ), &sTogezoWalkerStateParam, &sTogezoWalkerStateWanderParam );
        mChaseState    = new WalkerStateChase( this, al::getFrontPtr( this ), &sTogezoWalkerStateParam, &sTogezoWalkerStateChaseParam, false );
        mBlowDownState = new EnemyStateBlowDown( this, nullptr, nullptr, 0 );
        al::initNerveState( this, mWanderState, &NrvTogezo::Wander, "[State] 徘徊" );
        al::initNerveState( this, mChaseState, &NrvTogezo::Chase, "[State] 追いかけ" );
        al::initNerveState( this, mBlowDownState, &NrvTogezo::BlowDown, "[State] 吹っ飛び死" );
        makeActorAppeared();
}

#endif

extern "C" bool fn_00272a9c();
extern "C" bool fn_00259758( al::LiveActor*, const sead::Vector3f&, const WalkerStateParam* );

void Togezo::exeWander()
{
        al::updateNerveState( this );
        if ( !fn_00272a9c() && fn_00259758( this, al::getFront( this ), &sTogezoWalkerStateParam ) )
                al::setNerve( this, &NrvTogezo::Turn );
}

extern "C" bool fn_00262988( al::LiveActor*, sead::Vector3f* out, const sead::Vector3f&,
        float ); // turn (?)
extern "C" void fn_00258774( Togezo*, const WalkerStateParam* );

#ifdef NON_MATCHING // inline nops

void Togezo::exeTurn()
{
        if ( al::isFirstStep( this ) )
                al::startAction( this, "Turn" );
        fn_00258774( this, &sTogezoWalkerStateParam );
        if ( fn_00272a9c() )
        {
                al::setNerve( this, &NrvTogezo::Wander );
                return;
        }
        if ( fn_00262988( this, al::getFrontPtr( this ), rp::getPlayerPos(), 6.0 ) )
                al::setNerve( this, &NrvTogezo::Search );
}

#endif

#ifdef NON_MATCHING

// inline nops
void Togezo::exeSearch()
{
        if ( al::isFirstStep( this ) )
                al::startAction( this, "Search" );
        fn_00258774( this, &sTogezoWalkerStateParam );
        fn_00262988( this, al::getFrontPtr( this ), rp::getPlayerPos(), 6.0 );
        if ( al::isActionEnd( this ) )
        {
                if ( fn_00272a9c() )
                        al::setNerve( this, &NrvTogezo::Wander );
                else
                        al::setNerve( this, &NrvTogezo::Chase );
        }
}

#endif

extern "C" bool fn_0026b6cc( WalkerStateWander*, const sead::Vector3f& trans );

void Togezo::exeChase()
{
        if ( al::updateNerveStateAndNextNerve( this, &NrvTogezo::Wander ) )
                fn_0026b6cc( mWanderState, al::getTrans( this ) );
}

#ifdef NON_MATCHING // inline nops

void Togezo::exeAttack()
{
        if ( al::isFirstStep( this ) )
        {
                al::startAction( this, "AttackSuccess" );
                fn_00258774( this, &sTogezoWalkerStateParam );
        }
        if ( al::isActionEnd( this ) )
                al::setNerve( this, &NrvTogezo::Wander );
}

#endif

extern "C" void fn_00279158( Togezo*, const EnemyStateBlowDown* );

#ifdef NON_MATCHING
void Togezo::exeBlowDown()
{
        if ( al::updateNerveState( this ) )
        {
                fn_00279158( this, mBlowDownState );
                kill();
        }
}
#endif
```



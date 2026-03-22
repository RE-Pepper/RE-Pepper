#include "Enemy/WalkerStateChase.h"

#include <Nerve/alNerve.h>

#include "Enemy/WalkerStateChaseParam.h"

static WalkerStateChaseParam sDefaultParam( false, false, 2.0, 65, 150, 4.0, 15, "Run", "Wait" );

namespace NrvWalkerStateChase
{

NERVE_DEF( WalkerStateChase, Start )

} // namespace NrvWalkerStateChase

#ifdef NON_MATCHING

WalkerStateChase::WalkerStateChase( al::LiveActor* host, sead::Vector3f* frontPtr, const WalkerStateParam* walkParam, const WalkerStateChaseParam* runParam, bool b )
    : ActorStateBase( "ÉNÉäÉ{Å[í«Ç¢Ç©ÇØèÛë‘", host ), mFrontPtr( frontPtr ), mRunParam( runParam ),
      mWalkParam( walkParam ), _1C( b ), _20( nullptr )
{
        if ( runParam == nullptr )
                mRunParam = &sDefaultParam;
        initNerve( &NrvWalkerStateChase::Start );
}

#endif

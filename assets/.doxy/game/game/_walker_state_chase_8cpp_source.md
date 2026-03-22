

# File WalkerStateChase.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Enemy**](dir_0e41e8db2a159a2532eb8129063edf58.md) **>** [**WalkerStateChase.cpp**](_walker_state_chase_8cpp.md)

[Go to the documentation of this file](_walker_state_chase_8cpp.md)


```C++
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
    : ActorStateBase( "クリボー追いかけ状態", host ), mFrontPtr( frontPtr ), mRunParam( runParam ),
      mWalkParam( walkParam ), _1C( b ), _20( nullptr )
{
        if ( runParam == nullptr )
                mRunParam = &sDefaultParam;
        initNerve( &NrvWalkerStateChase::Start );
}

#endif
```



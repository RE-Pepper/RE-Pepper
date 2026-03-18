

# File CoinRotater.cpp

[**File List**](files.md) **>** [**Game**](dir_c33286056d2acf479cd8641ef845fec1.md) **>** [**src**](dir_d858f423bf5825f9a3db826b6a54a3cc.md) **>** [**MapObj**](dir_9fb1f6495822aa302d379b21d455a7ad.md) **>** [**CoinRotater.cpp**](_coin_rotater_8cpp.md)

[Go to the documentation of this file](_coin_rotater_8cpp.md)


```C++
#include "MapObj/CoinRotater.h"

#include <Scene/alSceneObjHolder.h>

#include "Scene/SceneObjFactory.h"

#ifdef NON_MATCHING
// need to find out what all the space at 0x68 is used for
CoinRotater::CoinRotater()
    : LiveActor( "コイン回転管理" )
{
}

#endif

const char* CoinRotater::getSceneObjName() const
{
        return "コインローテータ";
}

extern "C" void fn_00277de0( al::LiveActor*, const al::ActorInitInfo& );

void CoinRotater::initAfterPlacementSceneObj( const al::ActorInitInfo& info )
{
        fn_00277de0( this, info );
        makeActorAppeared();
}

namespace rp
{

void createCoinRotater()
{
        al::createSceneObj( SceneObjType_CoinRotater );
}

float getCoinRotateY()
{
        CoinRotater* rotater = static_cast<CoinRotater*>( al::getSceneObj( SceneObjType_CoinRotater ) );
        return rotater->getRotateY();
}

} // namespace rp
```





# File CoinRotater.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**MapObj**](dir_d5af9f6f62d27d9e3db1b7ff0fb6c0e1.md) **>** [**CoinRotater.cpp**](_coin_rotater_8cpp.md)

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





# File CoinRotater.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**MapObj**](dir_2096800ae80e9b320e335490a6d8aa70.md) **>** [**CoinRotater.h**](_coin_rotater_8h.md)

[Go to the documentation of this file](_coin_rotater_8h.md)


```C++
#pragma once

#include <LiveActor/alLiveActor.h>
#include <Scene/alISceneObj.h>

class CoinRotater : public al::LiveActor, public al::ISceneObj
{
private:
        float mRotateY;
        u8    _68[ 0x64 ];

public:
        float getRotateY()
        {
                return mRotateY;
        }

public:
        virtual const char* getSceneObjName() const;
        virtual void        initAfterPlacementSceneObj( const al::ActorInitInfo& info );

        virtual void movement();

public:
        CoinRotater();
};

namespace rp
{

void  createCoinRotater();
float getCoinRotateY();

} // namespace rp
```





# File CoinCharger.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**MapObj**](dir_2096800ae80e9b320e335490a6d8aa70.md) **>** [**CoinCharger.h**](_coin_charger_8h.md)

[Go to the documentation of this file](_coin_charger_8h.md)


```C++
#pragma once

#include <Nerve/alNerveExecutor.h>

namespace al
{
class AudioKeeper;
class LayoutInitInfo;
} // namespace al
class GameCountUp;

class CoinCharger : public al::NerveExecutor
{
private:
        GameCountUp*     mGameCountUp;
        void*            _C;
        void*            _10;
        al::AudioKeeper* mAudioKeeper;

public:
        CoinCharger( const al::LayoutInitInfo& info );
};
```





# File GameCountUp.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Layout**](dir_1e009ca70b4067525ad05e79ab8e6ed1.md) **>** [**GameCountUp.h**](_game_count_up_8h.md)

[Go to the documentation of this file](_game_count_up_8h.md)


```C++
#pragma once

#include <Layout/alLayoutActor.h>

namespace al
{
class LayoutInitInfo;
}

class GameCountUp : public al::LayoutActor
{
private:
        sead::Vector3f _30;
        bool           _3C;

public:
        GameCountUp( const al::LayoutInitInfo& info );
};
```



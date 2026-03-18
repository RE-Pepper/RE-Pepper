

# File alMathUtil.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Math**](dir_17d2d8808d20549c6aef9df204bad76e.md) **>** [**alMathUtil.cpp**](al_math_util_8cpp.md)

[Go to the documentation of this file](al_math_util_8cpp.md)


```C++
#include <Math/alMathUtil.h>

namespace al
{

bool isNearZero( float value, float range )
{
        return ( value < 0 ? -value : value ) < range;
}

} // namespace al
```



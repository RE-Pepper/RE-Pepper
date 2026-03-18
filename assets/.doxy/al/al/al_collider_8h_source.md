

# File alCollider.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Collision**](dir_d59a8b5ffa8fb2437785c15a7148fb09.md) **>** [**alCollider.h**](al_collider_8h.md)

[Go to the documentation of this file](al_collider_8h.md)


```C++
#pragma once

namespace al
{

class Collider
{
private:
        u8    _0[ 0xc0 ];
        float mGroundDistance;

public:
        float getGroundDistance()
        {
                return mGroundDistance;
        }

        void onInvalidate();
};

} // namespace al
```



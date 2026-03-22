

# File alAnimPlayerSimple.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Model**](dir_b30aa7a02aee64ce0942147420d20004.md) **>** [**alAnimPlayerSimple.h**](al_anim_player_simple_8h.md)

[Go to the documentation of this file](al_anim_player_simple_8h.md)


```C++
#pragma once

namespace al
{
class AnimInfoTable;

class AnimPlayerSimple
{
private:
        void*          _0;
        AnimInfoTable* mAnimInfoTable;
        void*          _8;
        void*          _C;
        void*          _10;
        void*          _14;
        void*          _18;

public:
        bool isAnimExist( const char* animName ) const;
        bool startAnim( const char* animName );
};

} // namespace al
```



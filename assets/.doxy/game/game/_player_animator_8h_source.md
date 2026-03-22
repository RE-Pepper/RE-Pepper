

# File PlayerAnimator.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerAnimator.h**](_player_animator_8h.md)

[Go to the documentation of this file](_player_animator_8h.md)


```C++
#pragma once

#include <prim/seadSafeString.h>

namespace al
{
class LiveActor;
}
class PlayerAnimFrameCtrl;
class PlayerModelHolder;

class IUsePlayerAnimator
{
public:
        virtual void  v_0()                                  = 0;
        virtual void  v_4()                                  = 0;
        virtual void  v_8()                                  = 0;
        virtual void  v_C()                                  = 0;
        virtual void  v_10()                                 = 0;
        virtual bool  isAnimEnd() const                      = 0;
        virtual bool  isAnim( const sead::SafeString& name ) = 0;
        virtual float getAnimFrame() const                   = 0;
        virtual void  v_20()                                 = 0;
        virtual void  v_24()                                 = 0;
        virtual void  v_28()                                 = 0;
        virtual void  v_2C()                                 = 0;
        virtual void  v_30()                                 = 0;
        virtual void  v_34()                                 = 0;
        virtual void  v_38()                                 = 0;
        virtual void  v_3C()                                 = 0;
        virtual void  v_40()                                 = 0;
        virtual void  v_44()                                 = 0;
        virtual void  v_48()                                 = 0;
        virtual void  v_4C()                                 = 0;
};

class PlayerAnimator : public IUsePlayerAnimator
{
private:
        al::LiveActor*       mHost;
        PlayerModelHolder*   mModelHolder;
        bool                 _C;
        bool                 _D;
        PlayerAnimFrameCtrl* mAnimFrameCtrl;
        bool                 _14;
        bool                 _15;

public:
        // virtual void v_0();
        // virtual void v_4();
        // virtual void v_8();
        // virtual void v_C();
        // virtual void v_10();
        // virtual bool isAnimEnd() const;
        // virtual bool isAnim(const sead::SafeString& name);
        virtual float getAnimFrame() const;
        // virtual void v_20();
        // virtual void v_24();
        // virtual void v_28();
        // virtual void v_2C();
        // virtual void v_30();
        // virtual void v_34();
        // virtual void v_38();
        // virtual void v_3C();
        // virtual void v_40();
        // virtual void v_44();
        // virtual void v_48();
        // virtual void v_4C();
public:
        PlayerAnimator( al::LiveActor* host, PlayerModelHolder* modelHolder );
};
```



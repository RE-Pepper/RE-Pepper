

# File PlayerAudio.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerAudio.h**](_player_audio_8h.md)

[Go to the documentation of this file](_player_audio_8h.md)


```C++
#pragma once

class IUsePlayerAudio
{
public:
        virtual void v0();
        virtual void v1();
        virtual void v2();
        virtual void v3();
        virtual void tryStartSePowerUp( bool isPowerDown );
        virtual void v5();
        virtual void v6();
        virtual void v7();
        virtual void triggerDead();
        virtual void v9();
        virtual void v10();
};

class PlayerAudio : public IUsePlayerAudio
{
public:
        PlayerAudio();
};
```



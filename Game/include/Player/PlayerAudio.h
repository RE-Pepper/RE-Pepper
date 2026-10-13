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

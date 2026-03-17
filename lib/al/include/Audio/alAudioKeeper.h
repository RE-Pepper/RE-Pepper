#pragma once

namespace al
{

class AudioKeeper
{
public:
        void update();
};

class IUseAudioKeeper
{
public:
        virtual void v1() {}
        virtual void v2() {}

        virtual AudioKeeper* getAudioKeeper() const = 0;
};

} // namespace al

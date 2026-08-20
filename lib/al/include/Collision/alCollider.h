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

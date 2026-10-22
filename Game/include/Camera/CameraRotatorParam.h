#pragma once

namespace al
{
class ByamlIter;
}

class CameraRotatorParam
{
private:
        float mAngleMax;

public:
        void init( const al::ByamlIter* ticket );

public:
        CameraRotatorParam();
};

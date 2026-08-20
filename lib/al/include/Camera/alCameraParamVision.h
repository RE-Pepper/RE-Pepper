#pragma once

namespace al
{

class ByamlIter;

class CameraParamVision
{
private:
        float mFovyDegree;
        float mStereovisionDistance;
        float mStereovisionDepth;
        float mNearClipDistance;
        float mFarClipDistance;

public:
        bool init( const ByamlIter* ticket );

public:
        CameraParamVision();
};

} // namespace al

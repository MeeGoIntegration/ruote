
#
# Testing Ruote
#
# Sun Jun 14 17:30:43 JST 2009
#

require File.dirname(__FILE__) + '/../test_helper.rb'

require 'ruote/exp/condition'


class ConditionTest < Test::Unit::TestCase

  class FakeExpression
    include Ruote::ConditionMixin

    def initialize (h)
      @h = h
    end
    def attribute (k)
      @h[k]
    end
  end

  def assert_not_skip (result, h)

    fe = FakeExpression.new(h)

    assert_equal result, (not fe.skip?)
  end

  def test_if

    assert_not_skip false, :if => 'true == false'
    assert_not_skip false, :if => "'true' == 'false'"
    assert_not_skip false, :if => '"true" == "false"'
  end

  def test_unless

    assert_not_skip true, :unless => 'true == false'
    assert_not_skip false, :unless => 'false == false'
  end

  def test_set

    assert_not_skip true, :if => 'true set'
    assert_not_skip true, :if => "'true' set"
    assert_not_skip true, :if => '"true" set'

    assert_not_skip true, :if => 'true is set'
    assert_not_skip true, :if => '"true" is set'
    assert_not_skip true, :if => "'true' is set"
    assert_not_skip false, :if => 'true is not set'
  end
end


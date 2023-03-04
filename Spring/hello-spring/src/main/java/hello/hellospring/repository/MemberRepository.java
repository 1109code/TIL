package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

//@Repository // spring이 repository 임을 인식
public interface MemberRepository {
    Member save(Member member);
    // Optional : null 처리
    // Optional로 감싸서 null 반환
    Optional<Member> findById(Long id);
    Optional<Member> findByName(String name);
    List<Member> findAll();
}
